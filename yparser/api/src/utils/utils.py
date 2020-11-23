from selenium import webdriver
import requests
from yparser.api.src.js_code import JS_DROP_FILE
from yparser.api.src.consts import CHROMEDRIVER_PATH


def init_wd(headless=True):
    """
    Initializing Chrome Webdriver from selenium library
    """
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)
    return wd


def save_image_by_response(response, savename, url):
    if not response.ok:
        print(response, url)
    else:
        with open(savename, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)


def get_image_by_url(url, savename, use_async=True):
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
        save_image_by_response(response, savename, url)

    except Exception as e:
        print(url)
        print(e, url)


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
