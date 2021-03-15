import sys
import os

from src.consts import IN_COLAB


def download_incolab_chromedriver():
    if IN_COLAB:
        os.system('apt-get update')
        os.system('apt install chromium-chromedriver')
        #os.system('cp /usr/lib/chromium-browser/chromedriver /usr/bin')
        #sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
