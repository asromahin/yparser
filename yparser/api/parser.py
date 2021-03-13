from yparser.api.src.yandex_parser import YandexParser
import os


def parse_by_images(
        image_paths: list,
        save_path: str,
        limit: int = 200,
        download: bool = True,
        n_threads: int = 16,
        kill_instances: bool = True,
        prefix='',
        recursive=False,
        recursive_limit=10,
):
    yp = YandexParser(kill_instances=kill_instances, n_threads=n_threads)
    for i, image_path in enumerate(image_paths):
        sub_path = '_'.join([save_path, prefix, str(i)])
        if recursive:
            recursive_images = yp.get_by_image(image_path, limit=recursive_limit, download=False, save_path=sub_path)
            for r_i, r_image_path in enumerate(recursive_images):
                r_sub_path = '_'.join([sub_path, str(r_i)])
                yp.get_by_image(r_image_path, limit=limit, download=download, save_path=r_sub_path)
        else:
            yp.get_by_image(image_path, limit=limit, download=download, save_path=sub_path)


def parse_by_images_urls(
        image_urls: list,
        save_path: str,
        limit: int = 200,
        download: bool = True,
        n_threads: int = 16,
        kill_instances: bool = True,
        prefix='',
        recursive=False,
        recursive_limit=10,
):
    yp = YandexParser(kill_instances=kill_instances, n_threads=n_threads)
    for i, image_path in enumerate(image_urls):
        sub_path = '_'.join([save_path, prefix, str(i)])
        if recursive:
            recursive_images = yp.get_by_image_url(image_path, limit=recursive_limit, download=False, save_path=sub_path)
            if recursive_images:
                for r_i, r_image_urls in enumerate(recursive_images):
                    r_sub_path = '_'.join([sub_path, str(r_i)])
                    yp.get_by_image_url(r_image_urls, limit=limit, download=download, save_path=r_sub_path)
        else:
            yp.get_by_image_url(image_path, limit=limit, download=download, save_path=sub_path)

