from imagededup.methods import PHash#, CNN
import os
from tqdm import tqdm
import cv2
from shutil import copyfile, rmtree
import glob


os.mkdir('clean_data')
phasher = PHash(verbose=False)
#files = os.listdir('data')
files = glob.glob('D://Repositories/SHIFT_LAB_PARSER/data/**/**.jpg')
print(files)
encodings = {}
for i in tqdm(range(len(files))):
    fname = files[i].split('\\')[-1]
    dir_name = files[i].split('\\')[-2]
    save_name = '_'.join([dir_name, fname])
    #print(save_name)
    try:
        im = cv2.imread(files[i])
        if len(im.shape) == 3:
            encoding = phasher.encode_image(image_array=im)
            encodings[str(save_name)] = str(encoding)
            cv2.imwrite('clean_data/' + save_name, im)
            #copyfile(files[i], os.path.join('clean_data', save_name))
    except Exception as e:
        print(e)

pass_keys = []
remove_keys = []
for key in tqdm(encodings.keys()):
    cur_encoding = encodings[key]
    for another_key in encodings.keys():
        if key != another_key and another_key not in pass_keys and another_key not in remove_keys:
            another_encoding = encodings[another_key]
            score = phasher.hamming_distance(cur_encoding, another_encoding)
            if score < 10:
                if os.path.exists('clean_data/' + another_key):
                    os.remove('clean_data/' + another_key)
                    remove_keys.append(another_key)
    pass_keys.append(key)

#print(encodings)
#print(encodings[list(encodings.keys())[0]])
#duplicates = phasher.find_duplicates(encoding_map=encodings)
#duplicates = phasher.find_duplicates(image_dir='clean_data')

#print(duplicates)

"""
data = []
dkeys = list(duplicates.keys())
ind_key = 0
while True:
    print(len(dkeys))
    data.append(dkeys[ind_key])
    if len(duplicates[dkeys[ind_key]]) > 0:
        for j in range(len(duplicates[dkeys[ind_key]])):
            try: 
                dkeys.remove(duplicates[dkeys[ind_key]][j])
                os.remove('clean_data/'+duplicates[dkeys[ind_key]][j])
            except:
                pass
    ind_key += 1
    if ind_key >= len(dkeys)-1:
        break"""