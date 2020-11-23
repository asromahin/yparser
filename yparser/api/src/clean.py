from imagededup.methods import PHash
import os
from tqdm import tqdm
import cv2
import glob


def clean_data(source_path='../data', save_path='../clean_data', threshold=10, method=None):
    save_dir = save_path
    os.mkdir(save_dir)

    files = glob.glob(f'{source_path}/*/*/*/*.jpg', recursive=True)
    if method == 'phash':
        hasher = PHash()

    encodings = {}
    for i, file in tqdm(enumerate(files)):
        im = cv2.imread(file)
        if im is not None:
            if len(im.shape) == 3 and im.shape[-1] == 3:
                trig = True
                if method is not None:
                    hash1 = hasher.encode_image(image_array=im)
                    for key in encodings.keys():
                        hash2 = encodings[key]
                        dist = hasher.hamming_distance(hash1, hash2)
                        if dist < threshold:
                            trig = False
                            break
                if trig:
                    save_path = os.path.join(save_dir, str(i)+'.jpg')
                    if method is not None:
                        encodings[save_path] = hash1
                    cv2.imwrite(save_path, im)
    print(len(os.listdir(save_dir)))
    return encodings