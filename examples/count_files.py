import glob

files = glob.glob('../data/*/*/*/*.jpg', recursive=True)
print(len(files))