from api.parser.YandexParser import YandexParser
import os
os.environ['HTTPS_PROXY'] = 'http://localhost:3128'

YP = YandexParser('save_path')
image_url = "https://www.wikihow.com/images/thumb/7/75/Change-the-Default-Search-Engine-in-Yandex-Browser.png/460px-Change-the-Default-Search-Engine-in-Yandex-Browser.png.webp"
YP.get_by_image_url(image_url)