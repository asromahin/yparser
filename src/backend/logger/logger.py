from queue import Queue
import threading
import sys
import numpy as np
import wandb
import time
from collections import defaultdict

from backend.logger.messages import (
    CorrectSaveMessage,
    IncorrectSaveMessage,
    CorrectParseMessage,
    IncorrectParseMessage,
    ParseMessage,
    DownloadsMessage,
    CurrentStateScreenshotMessage,
)


class Logger(threading.Thread):
    def __init__(self, wandb_log=True):
        threading.Thread.__init__(self)
        self.queue = Queue()
        self.first_message = None
        self.wandb_log = wandb_log
        self.log_data = defaultdict(lambda: 0)
        if self.wandb_log:
            self.wandb_timestamp = time.time()

    def run(self):
        """Запуск потока"""
        while True:
            message = self.queue.get()

            if self.first_message is None:
                self.first_message = message

            self.read_message(message)

            self.queue.task_done()

            self.print()
            if self.wandb_log:
                if message.timestamp - self.wandb_timestamp > 1:
                    self.print_wandb()
                    self.wandb_timestamp = message.timestamp

    def read_message(self, message):
        #print(message)
        diff_timestamp = message.timestamp - self.first_message.timestamp
        if diff_timestamp != 0:
            if isinstance(message, DownloadsMessage):
                self.log_data['downloads_speed'] = (self.log_data['downloads_corrects'] + self.log_data[
                    'downloads_incorrects']) / diff_timestamp
            elif isinstance(message, ParseMessage):
                self.log_data['parse_speed'] = (self.log_data['parse_corrects'] + self.log_data[
                    'parse_incorrects']) / diff_timestamp

       # print(type(message), isinstance(message, DownloadsMessage), isinstance(message, ParseMessage))
        if isinstance(message, DownloadsMessage):
            self.log_data['downloads_queue_size'] = message.len_queue
        if isinstance(message, ParseMessage):
            self.log_data['parse_queue_size'] = message.len_queue

        if isinstance(message, CorrectSaveMessage):
            self.log_data['downloads_corrects'] += 1
        if isinstance(message, IncorrectSaveMessage):
            self.log_data['downloads_incorrects'] += 1

        if isinstance(message, CorrectParseMessage):
            self.log_data['parse_corrects'] += 1
        if isinstance(message, IncorrectParseMessage):
            self.log_data['parse_incorrects'] += 1

        if isinstance(message, CurrentStateScreenshotMessage) and self.wandb_log:
            wandb.log({message.id: [wandb.Image(message.screenshot, caption=message.id)]})

    def print(self):
        res_str = '\r'
        for key, item in self.log_data.items():
            if 'screenshot' in key:
                continue
            item = np.round(item, 2)
            res_str += f'{key}={item}\t'
        sys.stdout.write(res_str)

    def print_wandb(self):
        wandb.log(self.log_data)


