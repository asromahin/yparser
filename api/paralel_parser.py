import os
import threading
import time

from api.parser import parse_by_images, parse_by_images_urls
from api.src.utils.kill_instances import kill_chrome_instances
from api.src.utils.utils import get_chunks
from api.src.utils.logger import *


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
    t1 = time.perf_counter()
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    if 'debug.log' in os.listdir(os.getcwd()):
        os.remove(f'{os.getcwd()}\\debug.log')
    chunks = get_chunks(image_urls, paralel_threads)
    threads = []

    if show_progress:
        logger = Logger(paralel_threads, image_urls)
    else:
        logger = Logger(paralel_threads)

    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
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
    # time.sleep(1)

    if write_logger_to_txt:
        logger.end_logging(log_to_txt=True)
    else:
        logger.end_logging()

    t2 = time.perf_counter()
    print('\nCompleted in {:.2f} seconds.'.format(t2-t1))
    # if write_logger_to_txt:
    #     print('Writing log data to txt...')
    #     write_log_to_txt(log_path, 'log', num_threads=paralel_threads)
    #     print('Written to txt')
    # else:
    #     print_log_to_console(log_path, num_threads=paralel_threads)
    # if log_path.empty():
    #     print('\nLog path emptied')
