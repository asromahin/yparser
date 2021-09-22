import threading
from queue import Queue
import urllib
import urllib.request
import os
import uuid
import time


from yparser.src.pool import Pool, PoolInstance
from yparser.src.logger.messages import CorrectSaveMessage, IncorrectSaveMessage


class Downloader(PoolInstance):
    """Потоковый загрузчик файлов"""

    def __init__(self, input_queue, save_folder, logger_queue, output_queue=None):
        """Инициализация потока"""
        super(Downloader, self).__init__(input_queue, output_queue, logger_queue)
        self.save_folder = save_folder

    def run_func(self, url):
        """Запуск потока"""
        try:
            save_path = self.download_file(url)
            if self.logger_queue is not None:
                message = CorrectSaveMessage(
                    id=self.id,
                    timestamp=int(time.time()),
                    url=url,
                    save_path=save_path,
                    len_queue=self.input_queue.qsize(),
                )
                self.logger_queue.put(message)
        except BaseException as e:
            if self.logger_queue is not None:
                message = IncorrectSaveMessage(
                    id=self.id,
                    timestamp=int(time.time()),
                    url=url,
                    error=e,
                    len_queue=self.input_queue.qsize(),
                )
                self.logger_queue.put(message)

    def download_file(self, url):
        """Скачиваем файл"""
        handle = urllib.request.urlopen(url, timeout=5)
        fname = str(uuid.uuid4()) + '.jpg'
        fname = os.path.join(self.save_folder, fname)

        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)

        return fname


class DownloaderPool(Pool):
    def __init__(self, n_workers, save_folder, output_queue=None, logger_queue=None):
        self.save_folder = save_folder
        os.makedirs(self.save_folder, exist_ok=True)
        super(DownloaderPool, self).__init__(
            output_queue=output_queue,
            pool_instance=Downloader,
            n_workers=n_workers,
            save_folder=save_folder,
            logger_queue=logger_queue,
        )