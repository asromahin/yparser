Python script to download images from 'Yandex Pictures'.

Inspired by google-images-download


Libs that are necessary to install for the parser(if you don't have it installed yet):
pip install opencv-python
pip install numpy
pip install imagededup
pip install pandas
pip install tqdm
pip install requests
pip install shutil

//Install selenium and chrome driver:

apt-get update
apt install chromium-chromedriver
cp / usr / lib / chromium-browser / chromedriver / usr / bin
pip install selenium

// in some python script:

import sys

sys.path.insert (0, '/ usr / lib / chromium-browser / chromedriver')


Install for the application:

pip install PyQt4
pip install matplotlib

How to start the parser?

1. Go  to yandex.ru / yandex.com and select the category "pictures"
2. There is a camera icon next to the "find" button, click it.
3.Upload a photo of the item you like to parse
4. As a result, click once on one of the “similar photos” presented in the section. You will be redirected to a new page. 
5.Copy URL of this page
6. Then go to the YandexGraber.py script, find the line wd.get ('') and insert your URL here
7. Run the script from the console: python YandexGraber.py
If the download went quickly, much faster than an hour, this means that there was an "incomprehensible glitch", which is somehow connected with Yandex, I haven't figured it out yet. It is treated by restarting the script. In general, the expected time is about 2 hours for 1500 images. You may have other numbers.
8. The result is in the data folder
9. Then you can clean the folder from some broken images that were downloaded, as well as from duplicates, for this run the script clean_data.py
10. A new clean_data will appear.

