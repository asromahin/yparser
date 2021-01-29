from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from api.src.js_code import JS_DROP_FILE
import os


def init_wd(path='../chromedriver', headless=True):
    """
    Initializing Chrome Webdriver from selenium library
    """
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome(ChromeDriverManager(print_first_line=False).install(),
                          chrome_options=chrome_options)
    return wd


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
