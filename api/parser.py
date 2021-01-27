from api.src.yandex_parser import YandexParser
import os
from api.src.utils.logger import Logger


def parse_by_images(
        image_paths: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        chromedriver_path: str = 'chromedriver',
):
    yp = YandexParser(chromedriver_path=chromedriver_path, kill_instances=kill_instances, n_threads=n_threads)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for i, image_path in enumerate(image_paths):
        sub_path = os.path.join(save_path, str(i))
        yp.get_by_image(image_path, limit=limit, download_type=download_type, save_path=sub_path)


def parse_by_images_urls(
        image_urls: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        chromedriver_path: str = 'chromedriver',
        logger=Logger,
        thread_id=0
):
    yp = YandexParser(chromedriver_path=chromedriver_path,
                      kill_instances=kill_instances,
                      n_threads=n_threads,
                      logger=logger,
                      thread_id=thread_id)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for i, image_url in enumerate(image_urls):
        sub_path = os.path.join(save_path, f'URL {i + 1}')
        yp.get_by_image_url(image_url, limit=limit, download_type=download_type, save_path=sub_path)


def parse_by_text_requests(
        text_requests: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        chromedriver_path: str = 'chromedriver',
        logger=Logger,
        thread_id=0
):
    yp = YandexParser(chromedriver_path=chromedriver_path,
                      kill_instances=kill_instances,
                      n_threads=n_threads,
                      logger=logger,
                      thread_id=thread_id)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for i, text_request in enumerate(text_requests):
        sub_path = os.path.join(save_path, str(text_request))
        yp.get_by_text(text_request, sub_path, limit, download_type)