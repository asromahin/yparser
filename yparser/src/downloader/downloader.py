import threading
from queue import Queue
import urllib
import urllib.request
import os
import uuid
import time


from yparser.src.downloader.messages import CorrectSaveMessage, IncorrectSaveMessage
from yparser.src.downloader.stats import DownloaderStats


class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""

    def __init__(self, queue, save_folder, stats_queue=None):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue
        self.save_folder = save_folder
        self.stats_queue = stats_queue

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()

            # Скачиваем файл
            try:
                save_path = self.download_file(url)
                if self.stats_queue is not None:
                    message = CorrectSaveMessage(
                        timestamp=int(time.time()),
                        url=url,
                        save_path=save_path,
                        len_queue=self.queue.qsize(),
                    )
                    self.stats_queue.put(message)
            except BaseException as e:
                if self.stats_queue is not None:
                    message = IncorrectSaveMessage(
                        timestamp=int(time.time()),
                        url=url,
                        error=e,
                        len_queue=self.queue.qsize(),
                    )
                    self.stats_queue.put(message)

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
    def __init__(self, save_folder, n_workers, show_stats=True):
        self.save_folder = save_folder
        self.show_stats = show_stats
        if self.show_stats:
            self.downloader_stats = DownloaderStats()
            self.downloader_stats.setDaemon(True)
            self.downloader_stats.start()
        os.makedirs(self.save_folder, exist_ok=True)
        self.n_workers = n_workers
        self.links_queue = Queue()
        for i in range(n_workers):
            if self.show_stats:
                t = Downloader(self.links_queue, save_folder=self.save_folder, stats_queue=self.downloader_stats.stats_queue)
            else:
                t = Downloader(self.links_queue, save_folder=self.save_folder)
            t.setDaemon(True)
            t.start()

    def push_links(self, links):
        for link in links:
            self.links_queue.put(link)