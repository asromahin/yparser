import threading
from queue import Queue
import urllib
import urllib.request
import os
import uuid
import time


from src.logger.messages import CorrectSaveMessage, IncorrectSaveMessage
from src.logger.logger import Logger


class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""

    def __init__(self, queue, save_folder, logger=None):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.id = str(uuid.uuid4())
        self.queue = queue
        self.save_folder = save_folder
        self.logger = logger

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()

            # Скачиваем файл
            try:
                save_path = self.download_file(url)
                if self.logger is not None:
                    message = CorrectSaveMessage(
                        id=self.id,
                        timestamp=int(time.time()),
                        url=url,
                        save_path=save_path,
                        len_queue=self.queue.qsize(),
                    )
                    self.logger.queue.put(message)
            except BaseException as e:
                if self.logger is not None:
                    message = IncorrectSaveMessage(
                        id=self.id,
                        timestamp=int(time.time()),
                        url=url,
                        error=e,
                        len_queue=self.queue.qsize(),
                    )
                    self.logger.queue.put(message)

            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()

    def download_file(self, url):
        """Скачиваем файл"""
        handle = urllib.request.urlopen(url)
        fname = str(uuid.uuid4()) + '.jpg'
        fname = os.path.join(self.save_folder, fname)

        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)

        return fname


class DownloaderManager:
    def __init__(self, save_folder, n_workers, logger=None):
        self.save_folder = save_folder
        self.logger = logger
        os.makedirs(self.save_folder, exist_ok=True)
        self.n_workers = n_workers
        self.links_queue = Queue()
        for i in range(n_workers):
            t = Downloader(self.links_queue, save_folder=self.save_folder, logger=self.logger)
            t.setDaemon(True)
            t.start()

    def push_links(self, links):
        for link in links:
            self.links_queue.put(link)