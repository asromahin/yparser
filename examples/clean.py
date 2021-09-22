PATH = 'D://datasets/SegmentationCars/seg_cars_v1'


import cv2
import os
from imagededup.methods import PHash
from tqdm import tqdm

if __name__ == '__main__':
    phasher = PHash()

    files = os.listdir(PATH)
    for f in tqdm(files):
        im = cv2.imread(os.path.join(PATH, f))
        if f is None:
            os.remove(os.path.join(PATH, f))

    # Generate encodings for all images in an image directory
    encodings = phasher.encode_images(image_dir=PATH)

    # Find duplicates using the generated encodings
    duplicates = phasher.find_duplicates(encoding_map=encodings)

    for orig, fakes in duplicates.items():
      for fake in fakes:
        try:
          os.remove(os.path.join(PATH, fake))
        except:
          pass