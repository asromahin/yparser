import torch
import pandas as pd
import cv2
import numpy as np
import os
import glob
from tqdm import tqdm

def make_query(row):
    return ' '.join([row['mark'], row['model'], row['year'], 'во дворе'])

mmy_df = pd.read_csv('mmy.csv')
dfs = glob.glob('D://datasets/cars/mmy_small/**/*.csv')

print(dfs)
df_all = []
for d in tqdm(dfs):
    print(d)
    cdf = pd.read_csv(d)
    df_all.append(cdf)
df = pd.concat(df_all)
print(len(df), len(mmy_df))
mmy_df['query'] = mmy_df.apply(make_query, axis=1)

df = pd.merge(mmy_df, df, how='inner', on='query')
print(len(df))
#
# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
#
# # Images
# imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
#
# # Inference
# results = model(imgs)
#
# # Results
# results.print()
# results.save()  # or .show()
#
# results.xyxy[0]  # img1 predictions (tensor)
# results.pandas().xyxy[0]  # img1 predictions (pandas)
