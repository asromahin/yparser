import glob
import os

#os.listdir('../data')

files = glob.glob('../data/*/*/*/*.jpg', recursive=True)
print(len(files))