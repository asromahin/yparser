import subprocess
import os

from src.backend.consts import IN_COLAB


def download_incolab_chromedriver():
    if IN_COLAB:
        p = subprocess.run('apt-get update', shell=True, check=True)
        p = subprocess.run('apt install chromium-chromedriver', shell=True, check=True)
        #os.system('cp /usr/lib/chromium-browser/chromedriver /usr/bin')
        #sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
