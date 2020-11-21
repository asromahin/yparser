
from imagededup.methods import PHash
import os
from tqdm import tqdm
import cv2
import glob

save_dir = '../clean_data'
os.mkdir(save_dir)

files = glob.glob('../data/*/*/*/*.jpg', recursive=True)
phasher = PHash()

encodings = {}
for i, file in tqdm(enumerate(files)):
    im = cv2.imread(file)
    if im is not None:
        if len(im.shape) == 3 and im.shape[-1] == 3:
            hash1 = phasher.encode_image(image_array=im)
            trig = True
            for key in encodings.keys():
                hash2 = encodings[key]
                dist = phasher.hamming_distance(hash1, hash2)
                if dist < 10:
                    trig = False
                    break
            if trig:
                save_path = os.path.join(save_dir, str(i)+'.jpg')
                encodings[save_path] = hash1
                cv2.imwrite(save_path, im)

print(len(os.listdir(save_dir)))