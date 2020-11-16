from selenium import webdriver
import requests
from api.js_code import JS_DROP_FILE


def init_wd():
    """
    Initializing Chrome Webdriver from selenium library
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    return wd


def get_image_by_url(url, savename):
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

        if not response.ok:
            print(response, url)
        else:
            with open(savename, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except Exception as e:
        print(url)
        print(e, url)


# def get_image_by_url2(url, savename):
#     try:
#         urllib.request.urlretrieve(url, savename)
#         wget.download(url=url, out=savename)
#         fastai.core.download_url(url, savename, show_progress=False)
#         pass
#     except Exception as e:
#         print(url)
#         print(e, url)

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)
