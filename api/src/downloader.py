from api.src.utils.utils import get_image_by_url, get_chunks
import os
import asyncio

import aiohttp
import aiofiles
import threading


async def fetch(session, image_link, save_path):
    async with session.get(image_link) as resp:
        if resp.status == 200:
            f = await aiofiles.open(save_path, mode='wb')
            await f.write(await resp.read())
            await f.close()


async def download_images_async(image_links, save_dir):
    async with aiohttp.ClientSession() as session:
        for i, image_link in enumerate(image_links):
            try:
                await fetch(session, image_link, os.path.join(save_dir, str(i) + '.jpg'))
            except:
                pass


def download_images_sync(images_links, save_dir, log_path):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for i, image_link in (enumerate(images_links)):
        save_path = os.path.join(save_dir, str(i) + '.jpg')
        get_image_by_url(image_link, save_path, log_path)


class Downloader:
    def __init__(self, n_threads=16):
        self.n_threads = n_threads

    def download_images(self, images_links, save_dir, log_path, download_type=0):
        if download_type == 0:
            download_images_sync(images_links, save_dir, log_path)
        elif download_type == 1:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(download_images_async(images_links, save_dir))
        elif download_type == 2:
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            chunks = get_chunks(images_links, self.n_threads)
            for i, chunk in enumerate(chunks):
                sub_path = os.path.join(save_dir, str(i))
                if len(chunk) > 0:
                    x = threading.Thread(target=download_images_sync, args=(chunk, sub_path, log_path))
                    x.start()


