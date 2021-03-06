import time
import threading
from queue import Queue

from src.parser import utils
from src.downloader.downloader import DownloaderManager
from src.logger.messages import CorrectParseMessage, IncorrectParseMessage, CurrentStateScreenshotMessage
import uuid
from PIL import Image
import numpy as np
import io


class YandexParser(threading.Thread):
    def __init__(self, queue: Queue, download_manager: DownloaderManager, limits=[200], parse_type='url', logger=None):
        threading.Thread.__init__(self)
        self.id = str(uuid.uuid4())
        self.wd = utils.init_wd()
        self.url = ''
        self.queue = queue
        self.limits = limits
        self.download_manager = download_manager
        self.parse_type = parse_type
        self.logger = logger
        self.link: Link = None

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            link = self.queue.get()
            self.link = link

            # Скачиваем файл
            try:
                if self.parse_type == 'url':
                    parsed_links = self.get_by_image_url(link.link)
                elif self.parse_type == 'path':
                    parsed_links = self.get_by_image(link.link)
                else:
                    parsed_links = []
                message = CorrectParseMessage(
                    id=self.id,
                    url=link.link,
                    timestamp=int(time.time()),
                    len_queue=self.queue.qsize(),
                    parsed=parsed_links,
                )
                self.logger.queue.put(message)
            except BaseException as e:
                message = IncorrectParseMessage(
                    id=self.id,
                    url=link.link,
                    timestamp=int(time.time()),
                    len_queue=self.queue.qsize(),
                    error=e,
                )
                self.logger.queue.put(message)

            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()

    def set_url(self, url):
        self.url = url
        if self.wd.current_url != self.url:
            self.wd.get(self.url)
            time.sleep(1)

    def log_screen(self):
        screenshot_data = self.wd.get_screenshot_as_png()

        screenshot = Image.open(io.BytesIO(screenshot_data))

        message = CurrentStateScreenshotMessage(
            id=self.id,
            url=self.url,
            timestamp=int(time.time()),
            len_queue=self.queue.qsize(),
            screenshot=screenshot,
        )
        self.logger.queue.put(message)

    def get_image_link(self, elem):
        url = elem.get_attribute('href')
        d = url.split('&')
        for i in range(len(d)):
            if 'img_url' in d[i]:
                d2 = d[i].split('=')[1]
                url = d2.split('%3A')
                url = ':'.join(url)
                url = url.split('%2F')
                url = '/'.join(url)
                return url

    def get_links_to_images(self):
        last_len = 0
        res_images = []
        while len(res_images) < self.limits[self.link.recurse_level]:
            imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            time.sleep(1)
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            if last_len == len(imgs):
                try:
                    elem = self.wd.find_element_by_class_name('button2_size_l')#[-1].click()
                    imgs = [self.get_image_link(img) for img in imgs]
                    res_images += imgs
                    self.get_images_by_links(imgs)
                    self.set_url(elem.get_attribute('href'))
                except BaseException as e:
                    break
            last_len = len(imgs)
        return res_images

    def get_images_by_links(self, images):
        images = list(set(images))
        self.download_manager.push_links(images)
        if self.link.recurse_level < len(self.limits)-1:
            for image in images:
                self.queue.put(Link(link=image, recurse_level=self.link.recurse_level+1))

    def get_by_text(self, text):
        url = "https://yandex.ru/images/search?from=tabbar&text={}".format(text.replace(' ', '%20'))
        self.get_by_url(url)

    def get_by_url(self, url):
        self.set_url(url)
        self.get_links_to_images()
        self.get_images_by_links()

    def to_navigation(self):
        self.wd.get('https://yandex.ru/images/')
        time.sleep(1)
        self.wd.find_element_by_class_name('input__cbir-button').click()
        time.sleep(1)

    def to_image_list(self):
        elem = self.wd.find_element_by_class_name('cbir-similar__thumbs-inner')
        elem = elem.find_element_by_tag_name('li')
        elem = elem.find_element_by_tag_name('a')
        start_url = elem.get_attribute('href')
        self.set_url(start_url)

    def wait_load_page(self, limit_seconds=60):
        start_url = self.wd.current_url
        seconds = 0
        while True:
            if self.wd.current_url != start_url or seconds >= limit_seconds:
                break
            time.sleep(1)
            seconds += 1
        time.sleep(1)

    def get_by_image(self, image_path):
        self.to_navigation()
        self.log_screen()
        target_panel = self.wd.find_element_by_class_name('cbir-panel__file-input')
        utils.drag_and_drop_file(target_panel, image_path)
        time.sleep(5)
        self.log_screen()
        self.to_image_list()
        images = self.get_links_to_images()
        return images

    def get_by_image_url(self, image_url):
        self.to_navigation()
        self.log_screen()
        cur_elem = self.wd.find_element_by_class_name('cbir-panel__input')
        target_panel = cur_elem.find_element_by_class_name('input__control')
        target_panel.click()
        target_panel.clear()
        target_panel.send_keys(image_url)
        time.sleep(2)
        self.log_screen()
        cur_elem.find_element_by_class_name('cbir-panel__search-button').click()
        time.sleep(5)
        self.log_screen()
        self.to_image_list()
        images = self.get_links_to_images()
        return images


class YandexParserManager:
    def __init__(self, downloader_manager: DownloaderManager, n_workers=1, limits=[200], parse_type='url', logger=None):
        self.queue = Queue()
        self.logger = logger
        for i in range(n_workers):
            t = YandexParser(self.queue, downloader_manager, limits=limits, parse_type=parse_type, logger=self.logger)
            t.setDaemon(True)
            t.start()

    def parse(self, links, wait_parse=True):
        for link in links:
            self.queue.put(Link(link=link, recurse_level=0))
        if wait_parse:
            self.queue.join()


class Link:
    def __init__(self, link, recurse_level):
        self.link = link
        self.recurse_level = recurse_level
