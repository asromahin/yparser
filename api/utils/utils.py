from selenium import webdriver

def init_wd():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    return wd


def get_image_by_url(url,savename):
    try:
            response = requests.get(url,timeout=5)
            if not response.ok:
                    print(response)
            with open(savename, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    except: print('error response',url)