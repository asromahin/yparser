import api.utils.utils as utils
from time import time
from tqdm import tqdm
import pandas as pd

class YandexParser():
    def __init__(self,limit=0,url=None):
        self.wd=utils.init_wd()
        self.limit=limit
        if(url):
            self.set_url(url)
    def set_url(self,url):
        self.url=url
    def get_links_to_images(self):
        self.wd.get(self.url)

        last_height = self.wd.execute_script("return document.body.scrollHeight")
        last_len = 0
        print('scroll page with images')
        while (True):
            imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            print(len(imgs))
            b = self.wd.find_element_by_class_name('more_direction_next')
            try:
                b.click()
            except:
                pass
            time.sleep(1)
            new_height = self.wd.execute_script("return document.body.scrollHeight")
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            if (last_len == len(imgs)):
                break;
            if (self.limit != 0):
                if (len(imgs) > self.limit):
                    break;
            last_height = new_height
            last_len = len(imgs)

        print('end scroll page with images')

        self.image_links = []
        for im in imgs:
            url = im.get_attribute('href')
            # print(url)
            d = url.split('&')
            for i in range(len(d)):
                if ('img_url' in d[i]):
                    d2 = d[i].split('=')[1]
                    url = d2.split('%3A')
                    url = ':'.join(url)
                    url = url.split('%2F')
                    url = '/'.join(url)
                    self.image_links.append(url)
                    break;
        print('end parse links for images')
        self.pdata = pd.DataFrame(self.image_links, columns=['url'])

    def get_images_by_links(self):

        print('start grab images')

        for i in tqdm(range(len(self.image_links))):
            utils.get_image(self.image_links[i], f'data/{i}.jpg')

        print('end grab images')
