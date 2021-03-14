import time
import threading
from queue import Queue

from yparser.src.parser import utils
from yparser.src.downloader.downloader import DownloaderManager


class YandexParser(threading.Thread):
    def __init__(self, queue: Queue, download_manager: DownloaderManager):
        threading.Thread.__init__(self)
        self.wd = utils.init_wd()
        self.url = ''
        self.queue = queue
        self.download_manager = download_manager

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()

            # Скачиваем файл
            try:
                self.get_by_image_url(url)
            except BaseException as e:
                print(e)

            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()

    def set_url(self, url):
        self.url = url
        if self.wd.current_url != self.url:
            self.wd.get(self.url)
            time.sleep(1)

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

    def get_links_to_images(self, limit=200):
        last_len = 0
        res_images = []
        while len(res_images) < limit:
            imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            time.sleep(1)
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            if last_len == len(imgs):
                try:
                    elem = self.wd.find_element_by_class_name('button2_size_l')#[-1].click()
                    for im in imgs:
                        res_images.append(self.get_image_link(im))
                    self.set_url(elem.get_attribute('href'))
                except BaseException as e:
                    break
            last_len = len(imgs)
        return res_images

    def get_images_by_links(self, images):
        images = list(set(images))
        self.download_manager.push_links(images)

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

    def get_by_image(self, image_path, limit=200, download=True):
        self.to_navigation()
        target_panel = self.wd.find_element_by_class_name('cbir-panel__file-input')
        utils.drag_and_drop_file(target_panel, image_path)
        self.wait_load_page()
        self.to_image_list()
        images = self.get_links_to_images(limit)
        if download:
            self.get_images_by_links(images)
        return images

    def get_by_image_url(self, image_url, limit=200, download=True):
        self.to_navigation()
        cur_elem = self.wd.find_element_by_class_name('cbir-panel__input')
        target_panel = cur_elem.find_element_by_class_name('input__control')
        target_panel.click()
        target_panel.clear()
        target_panel.send_keys(image_url)
        time.sleep(2)
        cur_elem.find_element_by_class_name('cbir-panel__search-button').click()
        time.sleep(5)
        self.to_image_list()
        images = self.get_links_to_images(limit)
        if download:
            self.get_images_by_links(images)
        return images


class YandexParserManager:
    def __init__(self, downloader_manager: DownloaderManager, n_workers=1):
        self.queue = Queue()
        for i in range(n_workers):
            t = YandexParser(self.queue, downloader_manager)
            t.setDaemon(True)
            t.start()

    def parse(self, links, wait_parse=True):
        for link in links:
            self.queue.put(link)
        if wait_parse:
            self.queue.join()

