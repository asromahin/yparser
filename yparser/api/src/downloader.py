from yparser.api.src.utils.utils import get_image_by_url, get_chunks
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


def download_images_sync(images_links, save_dir):
    for i, image_link in (enumerate(images_links)):
        save_path = '_'.join([save_dir, str(i) + '.jpg'])
        get_image_by_url(image_link, save_path)


class Downloader:
    def __init__(self, n_threads=16):
        self.n_threads = n_threads

    def download_images(self, images_links, save_dir):
        chunks = get_chunks(images_links, self.n_threads)
        for i, chunk in enumerate(chunks):
            sub_path = '_'.join([save_dir, str(i)])
            if len(chunk) > 0:
                x = threading.Thread(target=download_images_sync, args=(chunk, sub_path))
                x.start()


