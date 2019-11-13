# SHIFT_LAB_PARSER

# Необходимо установить для парсера: 
1) pip install opencv-python
2) pip install numpy
3) pip install imagededup
4) pip install pandas
5) pip install tqdm 
6) pip install requests
7) pip install shutil

# Установка selenium и chrome driver:

apt-get update

apt install chromium-chromedriver

cp /usr/lib/chromium-browser/chromedriver /usr/bin

pip install selenium

// in some python script:

import sys

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

# Необходимо установить для приложения:
1) pip install PyQt4
2) pip install matplotlib

# Как запускать парсер? 
1) Заходите на yandex.ru
2) Выбираете категорию "картинки"
3) Там есть иконка фотоаппарата возле кнопки "найти", жмёте её.
4) Загружаете фотографию электросчётчика
5) В полученном результате жмёте один раз на одну из представленных в разделе "похожие фотографии". Вас перекинет на новую страничку с поиском. Копируете url данной страницы
6) Затем идём в скрипт YandexGraber.py, находим строчку wd.get('') и вставляем сюда свой url 
7) Запускаем скрипт из консоли: python YandexGraber.py
8) Если загрузка быстро прошла, гораздо быстрее часа, это значит, что произошёл "непонятный глюк", который как-то связан с яндексом, пока не разобрался. Лечится перезапуском скрипта. Вообще ожидаемое время порядка 2 часов для 1500 изображений. У вас могут быть другие цифры.
9) Результат лежит в папке data 
10) Затем нужно почистить папку от плохо скаченных, а также от дубликатов, для этого запускаете скрипт clean_data.py
11) Появится новая clean_data - это и есть ваши данные, которые надо просмотреть и выбрать уже необходимые
