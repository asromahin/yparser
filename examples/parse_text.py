from yparser.api.parser import parse_by_images
import sys
sys.path.insert(0, '../')

image_paths = [
    'C:/Users/asrom/Desktop/Снимок экрана 2020-10-28 222305.png',
]

import os

print(os.path.exists(image_paths[0]))

parse_by_images(
    image_paths=image_paths,
    save_path='data',
    n_threads=32,
    chromedriver_path='../yparser/chromedriver/chromedriver.exe'
)

