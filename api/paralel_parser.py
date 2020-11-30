from api.parser import parse_by_images, parse_by_images_urls
from api.src.utils.kill_instances import kill_chrome_instances
from api.src.utils.utils import get_chunks, remove_jsons_and_csv, log, compile_to_csv
import threading
import os


def parse_paralel_by_images(
        image_paths: list,
        save_path: str,
        log_paths=None,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        remove_jsons_opt: bool = True,
        paralel_threads=2,
        chromedriver_path: str = 'chromedriver',
):
    if kill_instances:
        kill_chrome_instances()
    if remove_jsons_opt:
        remove_jsons()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_paths, paralel_threads)
    if log_paths is None:
        log_paths = [f'debug{i + 1}.json' for i in range(len(chunks))]
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
        remove_jsons_opt: bool = True,
        paralel_threads=2,
        log_paths=None,
        chromedriver_path: str = 'chromedriver',
):
    if kill_instances:
        kill_chrome_instances()
    if remove_jsons_opt:
        remove_jsons_and_csv()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_urls, paralel_threads)
    if log_paths is None:
        log_paths = [f'debug{i + 1}.json' for i in range(len(chunks))]
    threads = []
    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
        x = threading.Thread(target=parse_by_images_urls, args=(
            chunk,
            sub_path,
            log_paths[i],
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
    compile_to_csv(log_paths)