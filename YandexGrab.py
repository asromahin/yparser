from selenium import webdriver
import requests
import time
from tqdm import tqdm
import numpy as np
import shutil
import pandas as pd
import os
print('import all libs')
def init_wd():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    return wd
    
def get_image(url,savename):
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
os.mkdir('data')            
wd=init_wd() # init first time WebDriver
print('init wd')
#########################################################################################
# this url change with yours url 
url='https://yandex.ru/images/search?img_url=https%3A%2F%2Fwww.virage24.ru%2Fupload%2Fiblock%2F7e1%2F7e1d44035c13a6a11acdb12f0f0e539b.jpeg&cbir_id=2104436%2FIapc2H-9zYbUtn0AIt20Pw&rpt=imagelike&source=collections'
wd.get(url) 
#########################################################################################
print('get url:',url)
r=wd.get_screenshot_as_png()
with open('wd_init.png', 'wb') as f:
        f.write(r)
        
limit=0
last_height = wd.execute_script("return document.body.scrollHeight")
last_len=0
print ('start parse imgs')
while(True):
    imgs=wd.find_elements_by_class_name('serp-item__thumb')
    print(len(imgs))
    b=wd.find_element_by_class_name('more_direction_next')
    try: b.click()
    except: pass
    time.sleep(1)
    new_height = wd.execute_script("return document.body.scrollHeight")
    imgs=wd.find_elements_by_class_name('serp-item__link')
    if(last_len==len(imgs)):
        break;
    if(limit!=0):
        if(len(imgs)>limit):
            break;
    last_height = new_height
    last_len=len(imgs)        

print ('end parse imgs')

list_data=[]
for im in imgs:
    url=im.get_attribute('href')
    #print(url)
    d=url.split('&')
    for i in range(len(d)):
        if('img_url' in d[i]):
        
            d2=d[i].split('=')[1]
            url=d2.split('%3A')
            url=':'.join(url)
            url=url.split('%2F')
            url='/'.join(url)
            list_data.append(url)
            break;
    #print(list_data[0])
result_url=list_data

pdata=pd.DataFrame(result_url,columns=['url'])
pdata.to_csv('url_list.csv')

print ('start grab the images')

for i in tqdm(range(len(result_url))):
    get_image(result_url[i],f'data/{i}.jpg')
#print(result_url)
