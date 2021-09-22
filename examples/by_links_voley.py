from yparser.parser import YParser
image_urls = [
    'https://mipt.ru/upload/medialibrary/d03/volleyball.mipt2.jpg',
    'https://mipt.ru/upload/medialibrary/bf9/volleyball.mipt3.jpg',
    'https://lh3.googleusercontent.com/proxy/W8RSMi53irqdPbU15mbKDWvmO7GGANvDw0RKTm2K-qENoHnQlw326p4SgHn531V2Id_1TlAJduRbRhEZ5PpgjWBNB7u4rYxQr_ZjuZ0',
    'https://i.ytimg.com/vi/-62azoVPD6Y/maxresdefault.jpg',
    'https://lh3.googleusercontent.com/proxy/UwW99kyOB5mH79YeVoK3aKb8j14ioP3oaMiAf1xzpP0RbSO5MsBgVFpWDb_rJN3X0YaJNdk1AmcBS5Yj9TILIPUoW0k0T8s2SiwQkJoFGF47XR22qv3OgMqL',
    'https://bfmufa.ru/files/2016/01/volleyball_260116.jpg',
    'https://sputnik.kg/images/101783/14/1017831408.jpg',
    'https://volley39.ru/wp-content/uploads/2019/03/%D0%B2%D0%BE%D0%BB%D0%B5%D0%B9%D0%B1%D0%BE%D0%BB-%D0%BA%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4-20.jpg',
    'https://volley39.ru/wp-content/uploads/2020/03/MMFbGoNLRlk.jpg',
    'https://www.sobaka.ru/images/image/00/81/93/20/_normal.jpg',
    'https://i.ytimg.com/vi/04-SYUJ1Rgg/hqdefault.jpg',
    'https://sun9-41.userapi.com/c840226/v840226791/694e/Cq-uc633Vls.jpg',
    'https://sun9-6.userapi.com/c840226/v840226791/68fe/NZXJH6IE_Vs.jpg',
    'https://lh3.googleusercontent.com/proxy/XH5NavUjvurAy62eBaxiDY0IBaw-MMFipZF9MswfPAYf_PapUjTAW0PSAZUXK6-lzMb1XbkAlgdSOVZQq3sRRIfi86onhT5BgbukESTmH9Mc9pH_c7FQjVG8',
    'https://www.sobaka.ru/images/image/00/94/92/72/_normal.jpg',
    'https://coub-anubis-a.akamaized.net/coub_storage/coub/simple/cw_timeline_pic/ce975ec6b38/a5f5b3d70bc338cbd416b/med_1552295478_image.jpg',
    'https://coub-anubis-a.akamaized.net/coub_storage/coub/simple/cw_timeline_pic/743584ed6c2/4c643f26a77257d6ce02c/med_1552297288_image.jpg',
    'https://newsomsk.ru/images/old_class/2013/11/685c99dca1d5dc264e545dfa3071651c.jpg',
    'https://www.komus.ru/medias/sys_master/root/hb4/hf8/9724400402462/1.jpg',
    'https://aif-s3.aif.ru/images/018/519/0dcf52f61e0cbdde39830d466478b432.jpg',
    'https://lh3.googleusercontent.com/proxy/CSyPL4U-Lpz3Aoh8ekHAv9q6sQDSN_x3bdiQbJtgCLV34x77eEGM_C-xJo-ipx_ttu4Z4IAvg6dVFBnRBykpu0lNoZfoZzNz6xgVx7ucs0tpk0P-2Q',
    'https://mosregvolley.ru/wp-content/uploads/2020/02/FOTO-26-1024x683.jpg',
    'https://almetievsk-ru.ru/resize/shd//images/uploads/news/2018/3/20/e49c82af83929f8b11b0b3eba0134d90_XL.jpg',
    'https://zapad24.ru/uploads/posts/2019-05/1557303369_img_4713.jpg',
    'https://stavropolye.tv/uploads/news/202002/158254102364.jpg',
    'https://upload-d46147fab55529f5e07b04d1be8382db.hb.bizmrg.com/iblock/985/sWy8qxK9ulM.jpg',
    'https://zt116.ru/old/news/2019/04/IMG_5327.jpg',
    'https://sun9-25.userapi.com/c10741/u2355621/144606945/x_919f2338.jpg',
    'http://zhodinonews.by/wp-content/uploads/2018/01/valleyball2.jpg',
    'http://zhodinonews.by/wp-content/uploads/2018/01/valleyball1.jpg',
    'https://lh3.googleusercontent.com/proxy/uYty53ja8xm-XEzgrxXhMUS4noerXTzyuzs60gsb-VknyNBPgW_T8OYuWg3-Z8F7ccjstKZR66rHb7fQXF-1PxJUsYobIy_vtgxgv-vzKFFVKuietw',
    'https://lh3.googleusercontent.com/proxy/wu0WwBxuadDHvjCB0B6HJNRXgrBMhJAuflMt5bm-4C5aCnQXNQ0902unzBlLwQuyGWrYLnmoFcguVa7TIIDXtFDRxogdx5EUh1h3GNtUT4Emj9vVgRV8r-HeEbHztiy-yZGOqFo9s3bjEb27',
    'https://lh3.googleusercontent.com/proxy/z89oLZReWRWc_zAG0TLWRJhBLF0J6jxywvyk9swjtsQRlE1qtqrCzNfiE5ETvpFwqepYDeg4YY33dIu-K3g7MPZReNS7mnAz2oFqSaKEwXEc3ALiVRSNhi4-Cg_7_Q',
    'https://golk.by/wp-content/uploads/2020/03/img_5922-696x498.jpg',
    'https://rosphoto.com/images/u/articles/2101/oleshko-5.jpg',
    'https://lh3.googleusercontent.com/proxy/J2udVDkHqgnpF2W2dZBdw7zNd-EnKrLhp6fIk3e7lbzmeM8AngcwZq1XdlDKS8n0tN1jJrE0btn2EEdNCXzQTsi0X65JJJRlZJRcqFyjpuYMgMd7XGd6gXEoSEgXvd6OAEP2tTRXlMWmsxlQRQQyq0RnkjO3t6aWnQ',
    'https://img.stapravda.ru/!/a6/98/01/fa/29/79/32/51/7b/03/a6/92/6a/71/72/p92869-1606712886-320x180.jpg',

]
image_urls = list(set(image_urls))

SAVE_PATH = 'D://datasets'


parser = YParser(
    name='voley_dataset_v1',
    save_folder=SAVE_PATH,
    download_workers=16,
    parser_workers=3,
    limits=[20, 100],
    wandb_log=False,
)
parser.parse(links=image_urls)
