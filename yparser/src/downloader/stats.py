from queue import Queue
import threading
import sys

from yparser.src.downloader.messages import CorrectSaveMessage, IncorrectSaveMessage


class DownloaderStats(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stats_queue = Queue()
        self.num_errors = 0
        self.num_corrects = 0
        self.speed = 0
        self.bad_urls = []
        self.first_message = None

    def run(self):
        """Запуск потока"""
        while True:
            message = self.stats_queue.get()

            if self.first_message is None:
                self.first_message = message

            self.read_message(message)

            self.print()

            self.stats_queue.task_done()

    def read_message(self, message):
        diff_timestamp = message.timestamp - self.first_message.timestamp
        if diff_timestamp != 0:
            self.speed = self.num_corrects / diff_timestamp

        if isinstance(message, CorrectSaveMessage):
            self.num_corrects += 1
        if isinstance(message, IncorrectSaveMessage):
            self.bad_urls.append(message.url)
            self.num_errors += 1

    def print(self):
        sys.stdout.write(f"\rcorrrects={self.num_corrects}\twith errors={self.num_errors}\tspeed={self.speed}")


