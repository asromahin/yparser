from yparser.api.src.duplicates import calc_phash_from_path, calc_dist_hashes


if __name__ == '__main__':
    PATH1 = 'D://datasets/CreditCardDatasetYandex/0__3_5_10_2.jpg'
    PATH2 = 'D://datasets/CreditCardDatasetYandex/0__4_23_16_1.jpg'

    hash1 = calc_phash_from_path(PATH1)
    hash2 = calc_phash_from_path(PATH2)

    print(calc_dist_hashes([hash1, hash2]))