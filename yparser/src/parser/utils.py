from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from yparser.src.parser.js_code import JS_DROP_FILE
from yparser.src.consts import IN_COLAB
from yparser.src.utils.colab_downloader import download_incolab_chromedriver


def init_wd(headless=True):
    """
    Initializing Chrome Webdriver from selenium library
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-user-media-security=true")
    if headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    if IN_COLAB:
        download_incolab_chromedriver()
        wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    else:
        wd = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    return wd


def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)
