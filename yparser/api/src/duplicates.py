from collections import defaultdict
from typing import Sequence, Union
import os

import cv2
import numpy as np
from pqdm.processes import pqdm
from scipy.fftpack import dct


COEFFICIENT_EXTRACT = (8, 8)
TARGET_SIZE = (32, 32)


def preprocess_image(
    image: np.ndarray,
    target_size: tuple,
) -> np.ndarray:
    """Подготовка изображения в необходимый формат.

    :param image: Исходное изображения.
    :param target_size: Размер, к которому будет ресайзится изображения.
    :return: Преобразованное изображение.
    """
    image = cv2.resize(image, target_size)
    return image.astype('uint8')


def array_to_hash(hash_mat: np.ndarray) -> str:
    """Перевод массива numpy в строковое представление.

    :param hash_mat: Оригинальный хэш в виде numpy
    :return: Хэш
    """
    return ''.join('%0.2x' % pack_bits for pack_bits in np.packbits(hash_mat))  # noqa: WPS323


def calc_phash(image_array: np.ndarray) -> str:
    """Вычисляет хэш для изображения.

    :param image_array: Массив, включающий изображение.
    :return: Хэш
    """
    image_array = preprocess_image(image_array, target_size=TARGET_SIZE)
    dct_coef = dct(dct(image_array, axis=0), axis=1)
    dct_reduced_coef = dct_coef[:COEFFICIENT_EXTRACT[0], :COEFFICIENT_EXTRACT[1]]
    median_coef_val = np.median(np.ndarray.flatten(dct_reduced_coef)[1:])
    hash_mat = dct_reduced_coef >= median_coef_val
    return array_to_hash(hash_mat)


def hamming_distance(hash1: str, hash2: str) -> int:
    """Вычисляет расстояние между двумя хэшами.

    :param hash1: Первый хэш
    :param hash2: Второй хэш
    :return: Расстояние между хэшами
    """
    hash1_bin = bin(int(hash1, 16))[2:].zfill(64)   # noqa: WPS432
    hash2_bin = bin(int(hash2, 16))[2:].zfill(64)   # noqa: WPS432
    mask = [hash1 != hash2 for hash1, hash2 in zip(hash1_bin, hash2_bin)]
    return np.sum(mask)


def calc_phash_from_path(image_path: str) -> str:
    """Вычисляет PHash для изображения по пути image_path.

    :param image_path: Путь до изображения
    :return: Результат вычисления PHash для изображения
    """
    image_array = cv2.imread(image_path)
    return calc_phash(image_array)


def calc_hashes(images_paths: Sequence[str], threads: int) -> Sequence[str]:
    """Вычисляет все хэши для набора изображений в паралельном режиме и визуализирует прогресс.

    :param images_paths: Список путей до изображений
    :param threads: Количество потоков, в которых идёт вычисления.
    :return: Возвращает хэши, в соотвествии с порядком изображений.
    """
    return pqdm(images_paths, calc_phash_from_path, n_jobs=threads)


def calc_dist_between_hashes_by_hash(target_hash: str, hashes: Sequence[str]) -> Sequence[int]:
    """Вычисляет расстояние между определённым хэшем и списком сравниваемых хэшей.

    :param target_hash: Выбранный хэш для расчёта расстояний
    :param hashes: Список хэшей, с которыми вычисляеются расстояния
    :return: Список, размером с hashes, в каждом элементе которого, расстояние до каждого хэша.
    """
    all_distances = []
    for select_hash in hashes:
        dist = hamming_distance(target_hash, select_hash)
        all_distances.append(dist)
    return all_distances


def calc_dist_between_hashes_by_index(ind: int, hashes: Sequence[str]) -> Sequence[int]:
    """Вычисляет расстояния внутри hashes, выбирая хэш, для которого считаются расстояние, по индексу.

    :param ind: Индекс, по которому выбирается хэш
    :param hashes: Список всех хэшей
    :return: Список, размером с hashes, в каждом элементе которого, расстояние до каждого хэша.
    """
    target_hash = hashes[ind]
    return calc_dist_between_hashes_by_hash(target_hash, hashes)


def calc_dist_hashes(hashes: Sequence[str], threads: int = 16) -> Union[Sequence[Sequence[int]], np.ndarray]:
    """Вычисляет матрицу расстояний между хэшами в параллельном режиме, и визуализирует прогресс.

    :param hashes: Список хэшей
    :param threads: Количество потоков для параллельных вычислений
    :return: Двумерная матрица в ячейках которой лежат расстояния между соотвествующими по индексам изображениями
    """
    args = [{'ind': hash_index, 'hashes': hashes} for hash_index, select_hash in enumerate(hashes)]
    return pqdm(args, calc_dist_between_hashes_by_index, n_jobs=threads, argument_type='kwargs')


def find_duplicates_from_dist_matrix(
        dist_matrix: Union[np.ndarray, Sequence[Sequence]],
        images_paths: Sequence[str],
        threshold: int
):
    """Нахождение дубликатов по матрицу расстояний, и списку изображений, соответствующей ей в параллельном режиме.

    :param dist_matrix: Двумерная матрица расстояний
    :param images_paths: Пути до изображений
    :param threshold: Порог для расстояний, по которому определяется дубликат изображение, или нет.
    :return: Словарь, в котором ключ - это одно из изображений среди похожих, а значение - список похожих на него.
    """
    dist_matrix = np.array(dist_matrix)
    result_dict = defaultdict(list)
    mask = dist_matrix <= threshold
    points = np.where(mask)
    skip_paths = []
    for point_index, _ in enumerate(points[0]):
        path1 = images_paths[points[0][point_index]]
        path2 = images_paths[points[1][point_index]]
        if path1 in skip_paths or path1 == path2:
            continue
        else:
            skip_paths.append(path1)
            skip_paths.append(path2)
        result_dict[path1].append(path2)
    return result_dict


def find_duplicates(
        images_paths: Sequence[str],
        threshold: int = 10,
        threads: int = 16,
        use_delete_duplicates=False,
):
    """Вычисление всех хэшей, рассчёт матрицы расстояний и определение по ней дубликатов по выбранному порогу.

    :param images_paths: Список изображений
    :param threshold: Порог для поиска дубликатов. 10 - оптимальное число.
    :param threads: Количество потоков для параллелизации процесса.
    :return: Словарь, в котором ключ - это одно из изображений среди похожих, а значение - список похожих на него.
    """
    hashes = calc_hashes(images_paths, threads=threads)
    dist_matrix = calc_dist_hashes(hashes, threads=threads)
    duplicates_dict = find_duplicates_from_dist_matrix(dist_matrix, images_paths, threshold=threshold)
    if use_delete_duplicates:
        all_originals = delete_duplicates(duplicates_dict)
        return all_originals
    return duplicates_dict


def delete_duplicates(duplicates_dict):
    all_originals = []
    for original_path, duplicates_paths in duplicates_dict.items():
        for duplicate_path in duplicates_paths:
            if os.path.exists(duplicate_path):
                os.remove(duplicate_path)
        all_originals.append(original_path)
    return all_originals

