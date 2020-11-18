from api.src.yandex_parser import YandexParser
import os
import glob

#images = glob.glob('C:/Users/asrom/Desktop/ATA/Oven_new/*')
image_urls = [
    'https://kupi-plitu.ru/upload/iblock/b72/b7299f247cb043ad89e6462cfc571c73.jpg',
    'https://asko-russia.ru/upload/medialibrary/5b6/oven_15.jpg',
    'https://asko-russia.ru/upload/medialibrary/3a8/oven_18.jpg',
    'https://gastehmarket.ru/upload/iblock/365/0_b5b5e_706f8070_orig.jpg',
    'https://sovet-ingenera.com/wp-content/uploads/2019/08/elektroplita_v_kvartire.jpeg',
    'https://legko.com/disk/2/blogHQ/61/61d0d3b1f3b166b4310949ec9ff794ba.jpg',
    'https://static-ru.insales.ru/images/products/1/1124/38880356/ILVE_600MT-MP_I-2.jpg',
    'https://vitebsk.magazin-gefest.by/components/com_jshopping/files/img_products/full_komplekt-gefest-k28-2.jpg',
    'https://чёпочём.com/upload/resize_cache/iblock/a8e/1100_1100_078943735f710a67875c49e544806aeb8/a8eeeb9f5454a1adb15863ae123a631c.jpg',
    'http://brightbuild.ru/download/images/0/0/0091.jpg',
    'https://tehnika-spb.ru/upload/iblock/p70395_10071789_neff_c17cr22n1.jpg',
    'https://st35.stblizko.ru/images/product/269/279/560_original.jpg',
    'https://www.hausdorf.ru/upload/iblock/b20/hausdorf-dukhovoy-shkaf-neff-b46e74n0-1.jpg',
    'https://moyki-bt.ru/UserFiles/Image/paneli_kuppersberg/Kuppersberg_RC_699_ANX-4.jpg',
    'https://img.komfortbt.ru/content/5f2/5f29c6a447456c9695def124ca529be7.jpg',
    'https://shop-4all.ru/upload/iblock/95e/95e3b700f601336e696e5a10e9a39d8a.png',
    'https://www.e-mogilev.com/gimages/1200000/987570.3.jpg',
    'https://img.tehnomaks.ru/img/prod/full/c52b5202dcc57d6a2e39422e122bf8b071f94abc.jpg',
    'https://images.ru.prom.st/612786433_w640_h640_zapchasti-komplektuyuschie-i.jpg',
    'https://spb.premier-techno.ru/upload/iblock/40a/40a9d967856b37005a7d71d2cc2fb704.jpg',
    'https://www.hausdorf.ru/upload/iblock/811/Hausdorf-dukhovoy-shkaf-Ilve-600-CMP-WH-2.jpg',
    'https://www.btmoscow.ru/common/goodsImage/68/68368/844x554-68368_2.jpg',
    'https://spb.premier-techno.ru/upload/iblock/a01/a01b038dc9a024c18e2640affdc72692.jpg',
    'https://avatars.mds.yandex.net/get-market-ugc/248510/2a000001659ee7655c5b7b8daedb258a883f/1920-1920',
    'https://colstyle.ru/wa-data/public/shop/products/56/13/1356/images/3792/3792.970.jpg',
    'https://static.onlinetrade.ru/img/users_images/242845/b/elektricheskiy_dukhovoy_shkaf_lex_edp_093_iv_1559908822_1.jpg',
    'https://kupi-plitu.ru/upload/iblock/17f/17f484eae5527115c25b515bd7120977.jpg',
    'http://lavkabuy.ru/files/catalog/product/1562_5586.jpg',
    'https://boint.ru/upload/iblock/114/11405d675051ff8419b69679e18b7799.jpg',
    'https://ulbest.ru/image/cache/catalog/image/vstroika/darina/d6aba57c7625479378f70181bb2a9bdc-700x700.jpg',
    'https://severdv.ru/wp-content/uploads/2020/05/vstroennyj-duhovoj-shkaf-1.png',
    'https://static.onlinetrade.ru/img/items/b/korting_okb_1082_crc_575165_3.jpg',
    'https://kitchen-eco.ru/wp-content/uploads/2020/04/50-kak-pravilno-vibrat-duhovoi-shkaf-electricheskij-15.jpg',
    'https://ideas.homechart.ru/i/usersupload/352979_c004b728f8.jpg',
    'https://kitchen-eco.ru/wp-content/uploads/2020/04/50-kak-pravilno-vibrat-duhovoi-shkaf-electricheskij-19.jpg',
    'http://dmaster.kiev.ua/imagethumbw/podklyuchenie-tehniki/ustanovka-duhovogo-shkafa-600-800-184_6696.jpg',
    'http://cdn2.imgbb.ru/user/66/662136/201410/c69f1f51193606bf8f4aca8e6799a2a9.png',
    'https://asko-russia.ru/upload/medialibrary/89e/oven_7.jpg',
    'https://техникаоптом.рф/upload/iblock/7f5/7f5f38a232a2c5f9e66c4db69830bccb.jpg',
    'https://mca-partner.ru/wp-content/uploads/products_pictures/PureLine-ContourLine3.jpg',
    'https://tehno67.ru/670035-thickbox_default/dukhovoj-shkaf-franke-sm-66-m-xs-f.jpg',
    'http://kupimoiku.ru/wa-data/public/shop/products/29/93/19329/images/64035/64035.970x0.png',
    'https://mebel-alait.ru/gallery/kuhni-pryamye/10.jpg',
]
print(len(image_urls))
res_df = None
for i in range(10, len(image_urls)):
    image_url = image_urls[i]
    print(i, image_url)

    YP = YandexParser(os.path.join('../data', str(i)))
    with open(os.path.join('../data', str(i), 'url.txt'), 'w') as f:
        f.write(image_url)
        f.close()
    try:
        YP.get_by_image_url(image_url)
    except:
        print('-'*50)
        print('very bad error')
        print('-' * 50)
    YP.wd.close()
