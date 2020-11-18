from api.parser.YandexParser import YandexParser
import time

# Initializing YandexParser
start_time = time.time()
YP = YandexParser('data1')

# Insert the link where Similar Images Block is depicted
image_url = 'https://sun9-37.userapi.com/c857432/v857432140/1824ec/u1L-U5vjmQI.jpg?ava=1'
# Storing images in the 'data' folder
YP.get_by_image_url(image_url, limit=200, download_type=2)
