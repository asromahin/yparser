from yparser.parser import YParser
image_urls = [
    'https://www.professionalsport.ru/blog_entry_images/29639/original/priyom_miacha.jpg?1483025221',
    'http://volleysert.ru/wp-content/uploads/2015/09/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC-%D0%BC%D1%8F%D1%87%D0%B0-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%80%D1%83%D0%BA%D0%B0%D0%BC%D0%B8-%D1%81%D0%BD%D0%B8%D0%B7%D1%83-660x445.jpg',
    'https://rusvolley.ru/img/16693332_1920.png',
    'https://tvou-voleyball.ru/wp-content/uploads/2017/09/%D0%A2%D0%BE%D1%87%D0%BA%D0%B0-%D0%BA%D0%B0%D1%81%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BC%D1%8F%D1%87%D0%B0.jpg',
    'https://football-match24.com/wp-content/uploads/2020/03/pas-volleball-glav-600x330.jpg',
    'http://volleysert.ru/wp-content/uploads/2015/09/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC-%D0%BC%D1%8F%D1%87%D0%B0-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%80%D1%83%D0%BA%D0%B0%D0%BC%D0%B8-%D1%81%D0%BD%D0%B8%D0%B7%D1%831.jpg',
    'http://scsw.ru/wp-content/uploads/2017/05/IMG_1202-1024x683.jpg',
    'http://volleysert.ru/wp-content/uploads/2015/09/%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B8-%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%B0-%D0%BF%D0%BE%D0%B4%D0%B0%D1%87%D0%B8-%D0%B8-%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D1%8B-%D0%B8%D1%85-%D1%83%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.jpg',
    'http://volleysert.ru/wp-content/uploads/2015/08/maxresdefault-2.jpg',
    'https://lh3.googleusercontent.com/proxy/E9djagOVcno2eWw5NojQec_1xrYvabv26WiEpsFy2RMrsd7dmZGpSfTRZstiqAtHg1UEnzFCKQucWijhPkg',
    'http://sun9-10.userapi.com/impg/Ags7rCL9JrKDi7TkHLzzJJ1BZrin0M7H5pciIA/kuoVCsPF1wA.jpg?size=340x428&quality=96&sign=5b55a8ec9a9049f6891b9c7af9a6f05b&type=album',
    'https://resh.edu.ru/uploads/lesson_extract/3745/20190517171439/OEBPS/objects/m_ptls_11_3_1/5c5bd3ab8b141757fe1e62ce.jpg',
    'https://www.sovsport.ru/data/sovsport/preview/2000-01/16/images-2866-1538126723-800x557.jpg',
    'https://lh3.googleusercontent.com/proxy/PPps0MKpRHmO65NGObWxnuHgzfvtr99_Xeh0TmefANHUJnEFvzSLUZ_Zusr56S6d7qSfD_XyBLPp2Z0ZAlg',
    'https://sportsfan.ru/wp-content/uploads/2016/10/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC-%D0%BC%D1%8F%D1%87%D0%B0-%D0%B2-%D0%B2%D0%BE%D0%BB%D0%B5%D0%B9%D0%B1%D0%BE%D0%BB%D0%B5.jpg',
    'https://fiteria.ru/images/uprazhneniya-dlya-volejbola-v-domashnix-usloviyax-4.jpg',
]
image_urls = list(set(image_urls))

SAVE_PATH = 'D://datasets/voley_dataset_v1/activity'


parser = YParser(
    name='defend_down',
    save_folder=SAVE_PATH,
    download_workers=16,
    parser_workers=3,
    limits=[20, 100],
    wandb_log=False,
)
parser.parse(links=image_urls)
