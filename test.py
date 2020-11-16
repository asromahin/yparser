from api.parser.YandexParser import YandexParser
import os

YP = YandexParser('data')

image_url = ''       # Insert the link where Similar Pictures Block is depicted
YP.get_by_image_url(image_url)

