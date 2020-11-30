from selenium import webdriver
import requests
from api.src.js_code import JS_DROP_FILE
import json
import datetime
import os
import pandas as pd


def multi_replace_empty(string, symbol_list):
    for symbol in symbol_list:
        string = string.replace(symbol, '')
    return string


def record_json(json_dict, log_path, *data):
    symbol_list = ['{', '}', '"', "'", '\n']
    if len([*data]) == 1:
        json_dict[datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]] = multi_replace_empty(str(*data), symbol_list)
    else:
        data_list = multi_replace_empty(str([*data][0]), symbol_list)
        for i, item in enumerate([*data][1:]):
            # data_list.append(multi_replace_empty(str(item), symbol_list))
            data_list += multi_replace_empty((' ||| ' + str(item)), symbol_list)
        json_dict[datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]] = data_list
    with open(log_path, 'w', encoding='utf-8') as file:
        json.dump(json_dict, file, ensure_ascii=False, indent=1)


def log(log_path, *data):
    if log_path is None:
        # print('-' * 60)
        print(*data, datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3])
        # print('-' * 60)
    else:
        if log_path not in [i for i in os.listdir('../tests')]:
            json_dict = {}
            record_json(json_dict, log_path, *data)
        else:
            with open(log_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
            record_json(json_dict, log_path, *data)
    # print('-' * 60)
    # print(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3], [*data], sep=' ||| ')
    # print('-' * 60)


def compile_to_csv(log_paths: list,
                   file_name='test_log.csv'):
    data_list = []
    for json_file in log_paths:
        with open(json_file, 'r') as file:
            data = json.load(file)
        keys = list(data.keys())
        val = list(data.values())
        k_pd, v_pd = pd.Series(keys, name='Timestamp'), pd.Series(val, name='Response')
        data_list.append(k_pd)
        data_list.append(v_pd)
    db = pd.DataFrame(data_list).transpose()
    db.to_csv(file_name, encoding='windows-1251')


def init_wd(path='chromedriver', headless=True):
    """
    Initializing Chrome Webdriver from selenium library
    """
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(path, chrome_options=chrome_options)
    return wd


def save_image_by_response(response, savename, url, log_path):
    if not response.ok:
        log(log_path, str(response), url)
    else:
        with open(savename, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)


def get_image_by_url(url, savename, log_path, use_async=True):
    """
    Getting image by a given url using requests library
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    try:
        response = requests.get(
            url,
            timeout=5,
            stream=True,
            headers=headers,
        )
        save_image_by_response(response, savename, url, log_path)

    except Exception as e:
        log(log_path, str(e), url)


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)


def get_chunks(data, count):
    chunks = [[] for i in range(count)]
    it = 0
    for i in range(len(data)):
        if it % count == 0:
            it = 0
        chunks[it].append(data[i])
        it += 1
    return chunks


def remove_jsons_and_csv():
    print('\nRemoving jsons left...\n')
    jsons, csvs = 0, 0
    for item in os.listdir('../tests'):
        if '.json' in item:
            os.remove(f'../tests/{item}')
            jsons += 1
        if '.csv' in item:
            os.remove(f'../tests/{item}')
            csvs += 1
    if jsons != 0:
        print(f'{jsons} jsons removed.\n')
    if csvs != 0:
        print(f'{csvs} CSVs removed.\n')
