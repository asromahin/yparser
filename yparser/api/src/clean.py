import os
import cv2
import numpy as np
from pqdm.processes import pqdm
from yparser.api.src.duplicates import find_duplicates


def check_nan(file):
    im = cv2.imread(file)
    return im is None


def find_nan(images_paths, threads=16):
    images_paths = images_paths
    bad_mask = np.array(pqdm(images_paths, check_nan, n_jobs=threads), dtype='bool')
    bad_files = list(np.array(images_paths)[bad_mask])
    good_files = list(np.array(images_paths)[~bad_mask])
    return bad_files, good_files


def clean_nan(images_paths, threads=16):
    bad_files, good_files = find_nan(images_paths, threads)
    remove_files(bad_files)
    return good_files


def remove_files(images_paths):
    for image_path in images_paths:
        os.remove(image_path)


def full_clean(images_paths, threads=16, duplicates_threshold=10):
    good_files = clean_nan(images_paths, threads=threads)
    find_duplicates(good_files, threshold=duplicates_threshold, threads=threads, use_delete_duplicates=True)
