import os
import threading
import time

from api.parser import parse_by_images, parse_by_images_urls, parse_by_text_requests
from api.src.utils.kill_instances import kill_chrome_instances
from api.src.utils.utils import get_chunks
from api.src.utils.logger import Logger


def parse_paralel_by_images(
        image_paths: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        paralel_threads=2,
        chromedriver_path: str = 'chromedriver',
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_paths, paralel_threads)
    threads = []
    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
        x = threading.Thread(target=parse_by_images, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
            chromedriver_path,
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()


def parse_paralel_by_images_urls(
        image_urls: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        paralel_threads=2,
        chromedriver_path: str = 'chromedriver',
        write_logger_to_txt=False,
        show_progress=True
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    if 'debug.log' in os.listdir(os.getcwd()):
        os.remove(f'{os.getcwd()}\\debug.log')
    chunks = get_chunks(image_urls, paralel_threads)
    threads = []

    if show_progress:
        logger = Logger(image_urls, paralel_threads)
    else:
        logger = Logger(num_threads=paralel_threads)

    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, f'Thread {i + 1}')
        x = threading.Thread(target=parse_by_images_urls, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
            chromedriver_path,
            logger,
            i + 1
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()

    if write_logger_to_txt:
        logger.end_logging(log_to_txt=True)
    else:
        logger.end_logging()


def parallel_parse_by_text_requests(
        text_requests: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        parallel_threads=2,
        chromedriver_path: str = 'chromedriver',
        write_logger_to_txt=False,
        show_progress=True
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    if 'debug.log' in os.listdir(os.getcwd()):
        os.remove(f'{os.getcwd()}\\debug.log')
    chunks = get_chunks(text_requests, parallel_threads)
    threads = []

    if show_progress:
        logger = Logger(text_requests, parallel_threads)
    else:
        logger = Logger(num_threads=parallel_threads)

    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, f'Thread {i + 1}')
        x = threading.Thread(target=parse_by_text_requests, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
            chromedriver_path,
            logger,
            i + 1
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()

    if write_logger_to_txt:
        logger.end_logging(log_to_txt=True)
    else:
        logger.end_logging()