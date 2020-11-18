from api.utils.utils import get_image_by_url, save_image_by_response
import os
from tqdm import tqdm
import sys

import aiohttp
import asyncio
import async_timeout
from aiofile import async_open
from aiofile import AIOFile

import aiohttp
import aiofiles
import threading


async def fetch(session, image_link, save_path):
    async with session.get(image_link) as resp:
        if resp.status == 200:
            f = await aiofiles.open(save_path, mode='wb')
            await f.write(await resp.read())
            await f.close()


async def main(image_links, save_dir):
    async with aiohttp.ClientSession() as session:
        for i, image_link in enumerate(image_links):
            try:
                await fetch(session, image_link, os.path.join(save_dir, str(i) + '.jpg'))
            except:
                pass


def download_images_sync(images_links, save_dir, shift_iter=0):
    for i, image_link in (enumerate(images_links)):
        save_path = os.path.join(save_dir, str(shift_iter+i) + '.jpg')
        get_image_by_url(image_link, save_path)


class Downloader:
    def __init__(self, n_threads=16):
        #self.use_async = use_async
        self.n_threads = n_threads

    def download_images(self, images_links, save_dir, download_type=0):
        if download_type == 0:
            download_images_sync(images_links, save_dir)
        elif download_type == 1:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(images_links, save_dir))
        elif download_type == 2:
            chunk_size = len(images_links)//self.n_threads
            for i in range(0, len(images_links), chunk_size):
                x = threading.Thread(target=download_images_sync, args=(images_links[i:i+chunk_size], save_dir, i))
                x.start()


