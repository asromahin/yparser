from api.parser.YandexParser import YandexParser
import os
os.environ['HTTPS_PROXY'] = 'http://localhost:3128'

YP = YandexParser('save_path')
#images = ['']
image_url = "http://azovmed.com/images/444.png"
YP.get_by_image_url(image_url)

