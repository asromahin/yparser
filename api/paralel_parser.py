from api.parser import parse_by_images, parse_by_images_urls
from api.src.utils.kill_instances import kill_chrome_instances
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
    chunk_size = len(image_paths) // paralel_threads
    if chunk_size == 0:
        chunk_size = 1
    threads = []
    for i in range(0, len(image_paths), chunk_size):
        sub_path = os.path.join(save_path, str(i//chunk_size))
        x = threading.Thread(target=parse_by_images, args=(
            image_paths[i:i + chunk_size],
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
    chunk_size = len(image_urls) // paralel_threads
    if chunk_size == 0:
        chunk_size = 1
    threads = []
    for i in range(0, len(image_urls), chunk_size):
        sub_path = os.path.join(save_path, str(i//chunk_size))
        x = threading.Thread(target=parse_by_images_urls, args=(
            image_urls[i:i + chunk_size],
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
