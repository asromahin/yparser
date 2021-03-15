import subprocess
import os

from yparser.src.consts import IN_COLAB


def download_incolab_chromedriver():
    if IN_COLAB:
        p = subprocess.Popen(('apt-get', 'update'))
        p.wait()
        p = subprocess.Popen(('apt', 'install', 'chromium-chromedriver'))
        p.wait()
        #os.system('cp /usr/lib/chromium-browser/chromedriver /usr/bin')
        #sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
