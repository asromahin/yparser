from api.src.yandex_parser import YandexParser
import os
from api.src.utils.utils import log_path

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
):
    yp = YandexParser(chromedriver_path=chromedriver_path, kill_instances=kill_instances, n_threads=n_threads)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for i, image_url in enumerate(image_urls):
        sub_path = os.path.join(save_path, str(i))
        yp.get_by_image_url(image_url, limit=limit, download_type=download_type, save_path=sub_path)
    data = yp.load_log_data()
    log_path.append(data)