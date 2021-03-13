from yparser.api.src.utils import utils
from yparser.api.src.utils.kill_instances import kill_chrome_instances
import time
import os
from yparser.api.src.downloader import Downloader


def skip_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return None
    return wrapper


class YandexParser:
    def __init__(self, kill_instances=True, n_threads=16, use_log=True):
        """
        Initializing YandexParser class
        """
        if kill_instances:
            kill_chrome_instances()
        self.downloader = Downloader(n_threads=n_threads)
        self.wd = utils.init_wd()
        self.url = ''
        self.use_log = use_log

    def set_url(self, url):
        self.url = url
        if self.wd.current_url != self.url:
            self.wd.get(self.url)
            time.sleep(1)
            
    def log(self, *data):
        if self.use_log:
            print('-' * 60)
            print(*data)
            print('-' * 60)

    def get_image_link(self, elem):
        url = elem.get_attribute('href')
        # self.log(url)
        d = url.split('&')
        for i in range(len(d)):
            if 'img_url' in d[i]:
                d2 = d[i].split('=')[1]
                url = d2.split('%3A')
                url = ':'.join(url)
                url = url.split('%2F')
                url = '/'.join(url)
                return url

    def get_links_to_images(self, limit=200):
        last_len = 0
        self.log('scroll page with images')
        res_images = []
        while len(res_images) < limit:
            imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            self.log(len(res_images))
            time.sleep(1)
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            if last_len == len(imgs):
                try:
                    elem = self.wd.find_element_by_class_name('button2_size_l')#[-1].click()
                    for im in imgs:
                        res_images.append(self.get_image_link(im))
                    self.set_url(elem.get_attribute('href'))
                except BaseException as e:
                    self.log(e)
                    break
            last_len = len(imgs)
        self.log('end scroll page with images')
        return res_images

    def get_images_by_links(self, images, save_path):
        self.log('start grab images')
        images = list(set(images))
        self.downloader.download_images(images, save_dir=save_path)
        self.log('end grab images')

    def get_by_text(self, text):
        url = "https://yandex.ru/images/search?from=tabbar&text={}".format(text.replace(' ', '%20'))
        self.set_url(url)
        self.get_links_to_images()
        self.get_images_by_links()

    def get_by_url(self, url):
        self.set_url(url)
        self.get_links_to_images()
        self.get_images_by_links()

    def to_navigation(self):
        self.wd.get('https://yandex.ru/images/')
        self.log('open https://yandex.ru/images/')
        time.sleep(1)
        self.wd.find_element_by_class_name('input__cbir-button').click()
        time.sleep(1)

    def to_image_list(self):
        self.wd.save_screenshot('supertest.png')
        elem = self.wd.find_element_by_class_name('cbir-similar__thumbs-inner')
        elem = elem.find_element_by_tag_name('li')
        elem = elem.find_element_by_tag_name('a')
        start_url = elem.get_attribute('href')
        self.log('get url:', start_url)
        self.set_url(start_url)

    def wait_load_page(self, limit_seconds=60):
        start_url = self.wd.current_url
        seconds = 0
        while True:
            if self.wd.current_url != start_url or seconds >= limit_seconds:
                break
            time.sleep(1)
            seconds += 1
            self.log('while', seconds, 'seconds')
        time.sleep(1)

    @skip_error
    def get_by_image(self, image_path, save_path, limit=200, download=True):
        self.to_navigation()
        self.log(f'download image from {image_path}')
        target_panel = self.wd.find_element_by_class_name('cbir-panel__file-input')
        utils.drag_and_drop_file(target_panel, image_path)
        self.log('wait download')
        self.wait_load_page()
        self.to_image_list()
        self.log('go to page')
        images = self.get_links_to_images(limit)
        if download:
            self.get_images_by_links(images, save_path=save_path)
        return images

    @skip_error
    def get_by_image_url(self, image_url, save_path, save_screen='screenshot.png', limit=200, download=True):
        self.to_navigation()
        self.log(f'set image url {image_url}')
        cur_elem = self.wd.find_element_by_class_name('cbir-panel__input')
        target_panel = cur_elem.find_element_by_class_name('input__control')
        self.log(target_panel.get_attribute('value'))
        target_panel.click()
        target_panel.clear()
        target_panel.send_keys(image_url)
        #self.wd.get_screenshot_as_file(save_screen)
        time.sleep(2)
        cur_elem.find_element_by_class_name('cbir-panel__search-button').click()
        time.sleep(5)
        #self.wd.save_screenshot('test.png')
        self.to_image_list()
        images = self.get_links_to_images(limit)
        if download:
            self.get_images_by_links(images, save_path=save_path)
        return images

