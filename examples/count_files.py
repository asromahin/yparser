import glob

files = glob.glob('../stash_data/kaggle_leafs/data/*/*/*/*.jpg', recursive=True)
print(len(files))