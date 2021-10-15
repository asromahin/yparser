import time
from queue import Queue

from yparser.src.pool import PoolInstance, Pool
from yparser.src.parser import utils
from yparser.src.downloader.downloader import DownloaderPool
from yparser.src.logger.messages import CorrectParseMessage, IncorrectParseMessage, CurrentStateScreenshotMessage

from PIL import Image
import numpy as np
import io


class Link:
    def __init__(self, link, recurse_level):
        self.link = link
        self.recurse_level = recurse_level


class YandexParser(PoolInstance):
    def __init__(self, input_queue: Queue, output_queue: Queue = None, logger_queue: Queue = None, limits=[200], parse_type='url'):
        super(YandexParser, self).__init__(input_queue, output_queue, logger_queue)
        self.wd = utils.init_wd()
        self.limits = limits
        self.parse_type = parse_type

        self.url = ''
        self.link: Link = None

    def run_func(self, link: Link):
        self.link = link

        # Скачиваем файл
        try:
            if self.parse_type == 'url':
                parsed_links = self.get_by_image_url(link.link)
            elif self.parse_type == 'path':
                parsed_links = self.get_by_image(link.link)
            elif self.parse_type == 'text':
                parsed_links = self.get_by_text(link.link)
            else:
                parsed_links = []
            message = CorrectParseMessage(
                id=self.id,
                url=link.link,
                timestamp=int(time.time()),
                len_queue=self.input_queue.qsize(),
                parsed=parsed_links,
            )
            self.logger_queue.put(message)
        except BaseException as e:
            message = IncorrectParseMessage(
                id=self.id,
                url=link.link,
                timestamp=int(time.time()),
                len_queue=self.input_queue.qsize(),
                error=e,
            )
            print(e)
            self.logger_queue.put(message)

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
            len_queue=self.input_queue.qsize(),
            screenshot=screenshot,
        )
        self.logger_queue.put(message)

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
        #counter = 0
        res_images = []
        while len(res_images) < self.limits[self.link.recurse_level]:
            #imgs = self.wd.find_elements_by_class_name('serp-item__thumb')
            #time.sleep(1)
            imgs = self.wd.find_elements_by_class_name('serp-item__link')
            #print(len(imgs))
            if last_len == len(imgs):
                try:
                    elem = self.wd.find_elements_by_class_name('button2_size_l')[-1]#[-1].click()
                    imgs = [self.get_image_link(img) for img in imgs]
                    if len(res_images) + len(imgs) >= self.limits[self.link.recurse_level]:
                        dif = len(res_images) + len(imgs) - self.limits[self.link.recurse_level]
                        imgs = imgs[:-dif]
                    res_images += imgs
                    #self.wd.save_screenshot("test_"+str(counter)+'.png')
                    #counter += 1
                    self.get_images_by_links(imgs)
                    href = elem.get_attribute('href')
                    #print(href)
                    self.set_url(href)

                except BaseException as e:
                    #print(e)
                    break
            last_len = len(imgs)
        return res_images

    def get_images_by_links(self, images):
        images = list(set(images))
        if self.output_queue is not None:
            for image in images:
                self.output_queue.put(image)
        if self.link.recurse_level < len(self.limits)-1:
            for image in images:
                self.input_queue.put(Link(link=image, recurse_level=self.link.recurse_level+1))

    def get_by_text(self, text):
        url = "https://yandex.ru/images/search?from=tabbar&text={}".format(text.replace(' ', '%20')+'&isize=small')
        self.set_url(url)
        self.log_screen()
        return self.get_by_image_url(url, skip_to_nav=True)

    def to_navigation(self):
        self.wd.get('https://yandex.ru/images/')
        time.sleep(1)
        self.wd.find_element_by_class_name('input__cbir-button').click()
        time.sleep(1)

    def to_image_list(self):
        elem = self.wd.find_element_by_class_name('CbirSimilar-MoreButton')
        #elem = elem.find_element_by_tag_name('li')
        #elem = elem.find_element_by_tag_name('a')
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
        target_panel = self.wd.find_element_by_class_name('cbir-panel__dragzone')
        utils.drag_and_drop_file(target_panel, image_path)
        time.sleep(5)
        self.log_screen()
        self.to_image_list()
        images = self.get_links_to_images()
        return images

    def get_by_image_url(self, image_url, skip_to_nav=False):
        if not skip_to_nav:
            self.to_navigation()
            self.log_screen()
            #self.wd.find_element_by_class_name('input__cbir-button').click()
            #time.sleep(1)
            cur_elem = self.wd.find_element_by_class_name('CbirPanel-PopupBody')

            target_panel = cur_elem.find_element_by_tag_name('input')
            target_panel.click()
            target_panel.clear()
            target_panel.send_keys(image_url)
            time.sleep(1)
            self.log_screen()
            #print('hi')
            cur_elem.find_element_by_class_name('CbirPanel-UrlFormButton').click()
            time.sleep(5)
            self.log_screen()
            self.to_image_list()
        images = self.get_links_to_images()
        return images


class YandexParserPool(Pool):
    def __init__(self, n_workers=1, limits=[200], parse_type='url', output_queue=None, logger_queue=None):
        super(YandexParserPool, self).__init__(
            output_queue=output_queue,
            pool_instance=YandexParser,
            n_workers=n_workers,
            limits=limits,
            parse_type=parse_type,
            logger_queue=logger_queue,
        )

    def parse(self, links):
        for link in links:
            self.input_queue.put(Link(link=link, recurse_level=0))
