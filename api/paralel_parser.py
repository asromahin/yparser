import os
import threading
import time

from api.parser import parse_by_images, parse_by_images_urls
from api.src.utils.kill_instances import kill_chrome_instances
from api.src.utils.utils import get_chunks, parsed_links
from sys import stdout


def parse_paralel_by_images(
        image_paths: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        paralel_threads=2,
        chromedriver_path: str = 'chromedriver',
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_paths, paralel_threads)
    threads = []
    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
        x = threading.Thread(target=parse_by_images, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
            chromedriver_path,
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()


def print_log_to_console(log_path, num_threads):
    for i in range(num_threads):
        record = log_path.get()
        print('*' * 60)
        print(f'Record {i + 1}')
        print('*' * 60)
        for row in record:
            if '[[' not in str(row):
                print(str(row).replace('[', '').replace(']', '').replace("',", '').replace("'", ''))
            else:
                if str(row) == '[[]]':
                    print('No errors to log')
                else:
                    row = str(row).split(sep='], [')
                    for item in row:
                        print(item.replace('[[[', '').replace(']]]', ''))
        print('')


def print_percentage(parsed_links, image_urls):
    counter = 0
    while True:
        stdout.write('\r{:.0f}% | {}/{} links parsed'.format(counter / len(image_urls) * 100,
                                                                 counter,
                                                                 len(image_urls)))
        url = parsed_links.get()
        counter += 1
        parsed_links.task_done()


def write_log_to_txt(log_path, filename, num_threads):
    with open(f'{filename}.txt', 'w') as file:
        for i in range(num_threads):
            record = log_path.get()
            file.write('*' * 60 + '\n')
            file.write(f'Record {i + 1}' + '\n')
            file.write('*' * 60 + '\n')
            for row in record:
                if '[[' not in str(row):
                    file.write(str(row).replace('[', '').replace(']', '').replace("',", '').replace("'", '') + '\n')
                else:
                    if str(row) == '[[]]':
                        file.write('No errors to log' + '\n')
                    else:
                        row = str(row).split(sep='], [')
                        for item in row:
                            file.write(item.replace('[[[', '').replace(']]]', '') + '\n')
            file.write('\n')


def parse_paralel_by_images_urls(
        image_urls: list,
        save_path: str,
        limit: int = 200,
        download_type: int = 2,
        n_threads: int = 16,
        kill_instances: bool = True,
        paralel_threads=2,
        chromedriver_path: str = 'chromedriver',
        write_logger_to_txt=False
):
    if kill_instances:
        kill_chrome_instances()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    chunks = get_chunks(image_urls, paralel_threads)
    threads = []

    counter = threading.Thread(target=print_percentage, args=[parsed_links, image_urls], daemon=True)
    counter.start()

    for i, chunk in enumerate(chunks):
        sub_path = os.path.join(save_path, str(i))
        x = threading.Thread(target=parse_by_images_urls, args=(
            chunk,
            sub_path,
            limit,
            download_type,
            n_threads,
            False,
            chromedriver_path,
        ))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()
    time.sleep(2)

    print('\n\n')
    parsed_links.join()

    from api.src.utils.utils import log_path
    if write_logger_to_txt:
        print('Writing log data to txt...')
        write_log_to_txt(log_path, 'log', num_threads=paralel_threads)
        print('Written to txt')
    else:
        print_log_to_console(log_path, num_threads=paralel_threads)
    if log_path.empty():
        print('\nLog path emptied')
