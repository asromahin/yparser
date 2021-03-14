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
        self.bad_urls = []

    def run(self):
        """Запуск потока"""
        while True:
            message = self.stats_queue.get()

            self.read_message(message)

            self.print()

            self.stats_queue.task_done()

    def read_message(self, message):
        if isinstance(message, CorrectSaveMessage):
            self.num_corrects += 1
        if isinstance(message, IncorrectSaveMessage):
            self.bad_urls.append(message.url)
            self.num_errors += 1

    def print(self):
        print('\r')
        print(f"corrrects={self.num_corrects}\twith errors={self.num_errors}")


