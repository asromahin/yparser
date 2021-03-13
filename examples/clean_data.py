from yparser.api.src.duplicates import find_duplicates
from yparser.api.src.clean import clean_nan, full_clean
import glob
import os

if __name__ == '__main__':
    SAVE_PATH = 'D://datasets/WebCamHeadsets'

   # files = glob.glob(SAVE_PATH+'/*')
    files = [SAVE_PATH+'/'+f for f in os.listdir(SAVE_PATH)]

    #print(files[:10])

    full_clean(files, threads=16, duplicates_threshold=10)


