import cv2
import numpy as np
from tqdm import tqdm
import os

files=os.listdir('data')
minshape=(500,500)
maxshape=(0,0)
counter=0
counter_miss=0
for i in tqdm(range(len(files))):
    try: 
        im=cv2.imread('data/'+files[i],cv2.IMREAD_GRAYSCALE)
        if(im.shape<minshape):
            minshape=im.shape
        if(im.shape>maxshape):
            maxshape=im.shape
        if(im.shape>(300,300)):
            counter+=1
    except: 
        counter_miss+=1
print(minshape,maxshape,counter,counter_miss)