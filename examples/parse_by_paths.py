from yparser.src.downloader.downloader import DownloaderManager
from yparser.src.parser.yandex_parser import YandexParserManager
import os

FOLDER = 'D://datasets/test_parser'
image_urls = os.listdir(FOLDER)
image_urls = ['/'.join([FOLDER, url]) for url in image_urls]
image_urls = list(set(image_urls))

SAVE_PATH = 'D://datasets/test_parser_paths'


DM = DownloaderManager(SAVE_PATH, n_workers=48)
YPM = YandexParserManager(DM, n_workers=4, parse_type='path')
YPM.parse(links=image_urls)
