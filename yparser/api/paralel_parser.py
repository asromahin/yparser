from yparser.api.parser import parse_by_images, parse_by_images_urls
from yparser.api.src.utils.kill_instances import kill_chrome_instances
from yparser.api.src.utils.utils import get_chunks
import threading
import os


def parse_paralel_by_images(
        image_paths: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        paralel_threads=2,
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
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_urls, paralel_threads)
    threads = []
    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
        x = threading.Thread(target=parse_by_images_urls, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()
