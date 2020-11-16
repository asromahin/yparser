from api.parser.YandexParser import YandexParser
import os

YP = YandexParser('data')

image_url = 'https://yandex.ru/images/search?rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F2473989%2FxCvlKLoQ-M1xmxNwyLhtGQ%2Forig&cbir_id=2473989%2FxCvlKLoQ-M1xmxNwyLhtGQ&from=tabbar'
YP.get_by_image_url(image_url)

