PATH = 'D://datasets/cars/mmy_small'


import cv2
import os
from imagededup.methods import PHash
from tqdm import tqdm

if __name__ == '__main__':
    phasher = PHash()

    paths = os.listdir(PATH)
    paths = sorted([os.path.join(PATH, path) for path in paths])
    for path in paths:
        print(path)
        files = os.listdir(path)
        for f in tqdm(files):
            if '.csv' in f:
                continue
            im = cv2.imread(os.path.join(path, f))
            if im is None:
                os.remove(os.path.join(path, f))

        # Generate encodings for all images in an image directory
        encodings = phasher.encode_images(image_dir=path)

        # Find duplicates using the generated encodings
        duplicates = phasher.find_duplicates(encoding_map=encodings)

        for orig, fakes in duplicates.items():
          for fake in fakes:
            try:
              os.remove(os.path.join(path, fake))
            except:
              pass