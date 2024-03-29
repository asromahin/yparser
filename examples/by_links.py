from yparser.parser import YParser
image_urls = [
    'https://pbs.twimg.com/media/E9Zm0EBVUAgAtsi.jpg',
    'https://im0-tub-ru.yandex.net/i?id=3789c7a3d760abd9a6b2075efbe486b7-l&n=13',
    'https://sun9-54.userapi.com/c4333/u38426379/-6/x_02fc5033.jpg',
    'https://im0-tub-ru.yandex.net/i?id=5d41aedf135232a35d66a23daf0e66fd-sr&n=13',
    'https://im0-tub-ru.yandex.net/i?id=ef054e7f8e5340e964de36568e9380dd-l&n=13',
    'https://sun9-21.userapi.com/impg/7scsyGiqTBq4YcoErL8XGwfqPzj-vCBCSh_4Nw/iIenRJrdx6Q.jpg?size=130x272&quality=96&sign=5ac20e56e4bf3601e6f3f710f2d62fc4&type=album',
    'https://sun9-14.userapi.com/alrq4mKJ94sofZbtNRTYGF7HNrfaEdc5h-Ht5g/v-N42_WXmU4.jpg',
    'https://im0-tub-ru.yandex.net/i?id=c085c275eb09e6cdfc764a10727fe073-l&n=13',
    'https://sun9-47.userapi.com/c855620/v855620994/1db9ec/WbN_H1zQBuE.jpg?ava=1',
    'https://im0-tub-ru.yandex.net/i?id=0a1dea88e3ba6badb4bb3f29b7814f7e-l&n=13',
    'https://i.ytimg.com/vi/31Tu-yuTe5g/maxresdefault.jpg',
    'https://sun1-96.userapi.com/s/v1/if1/2hRlqGdMGj5M3kiy3PqH_Zz4i8saPlPoB2XvuS-Ojh_dS-MxyJ7zuZOQB1CzQ6YKyKAn2M3C.jpg?size=400x0&quality=96&crop=0,67,404,404&ava=1',
    'https://1.bp.blogspot.com/-ZwVxX7tTZYU/V9RCDJ8SoxI/AAAAAAAAMXA/9f8X01aqziIsRy2SD2a1ZKnzXs1sXR6qgCLcB/s640/product%2Bexperience%2B3.jpg',
    'https://sun9-39.userapi.com/impg/DKMoKN6C8lQPeCBrEb0wWJes3yxPVWnj5ihFCA/092n6GqWmvc.jpg?size=340x604&quality=96&sign=f5e5750189927c318ac5ec93cbc87b97&type=album',
    'https://im0-tub-ru.yandex.net/i?id=db633c1b796da7645ccadcaa9e95899d-l&n=13',
    'https://sun9-21.userapi.com/impf/UGkcRYp68h28qtg8K5rFzCkvVFS3Hqq8s2soig/EpugFupmxkU.jpg?size=320x569&quality=96&sign=818559d227641bd0bb9ef657dfb980df&c_uniq_tag=8r71ZflArU3Jk-ZT_EfzhFqFzFYA8Owj4izzx2JEk1E&type=album',
    'https://im0-tub-ru.yandex.net/i?id=3e3a8cd7e2c634c81df0982945d35b1d-l&n=13',
    'https://sun1-87.userapi.com/impf/PhB6sBz2op7PEnFGNHqYdjDRUworcemir-hcMQ/medMJAjzZic.jpg?size=400x0&quality=90&crop=5,26,573,573&sign=fee152cdcaeed0c5ac462935fbe4c145&c_uniq_tag=R_G89HG54d1gyEOQ0Tr9P3IR519M7Wiv9EkwSzYsH8Q&ava=1',
    'https://im0-tub-ru.yandex.net/i?id=541996602e01fe68bac754314f015ce5-l&n=13',
    'https://pm1.narvii.com/6848/f2c3781cd41558d49808c38edab46be0de62eb59v2_hq.jpg',
    'https://sun1-20.userapi.com/s/v1/ig2/We8qemUNgFxJqjijVSjGEsx8nv6BbxytnEWFe4lZ4tOJnGnYR_n1aLDugm2l2lN2g2L71eCvRjim4QV6l9mW26iZ.jpg?size=400x0&quality=96&crop=8,221,750,750&ava=1',
    'https://abakan-news.ru/wp-content/uploads/2019/09/2019-09-27_11-46-53.png',
    'https://im0-tub-ru.yandex.net/i?id=130028df6fcf50e988b342c2ba1bbb12-l&n=13',
    'https://i.ytimg.com/vi/hLIH0x-2M60/maxresdefault.jpg',
    'https://im0-tub-ru.yandex.net/i?id=72cbb6326d6b1211f0f0d4483db002dc-l&n=13',
    'https://i.ytimg.com/vi/it9KjjLCP64/maxresdefault.jpg',
    'https://im0-tub-ru.yandex.net/i?id=d1da3722fc97d61c67626d9b5f402e0e-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=1baef84abeae298a326fae4b90503612-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=0544f0a424e71407b6f8d6e1799b12d7-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=fd5cbc0bd30fa2e6ff030a7b99578e38-l&n=13',
    'https://sun9-34.userapi.com/c858320/v858320747/9f8c6/tFa8b9_KvuA.jpg',
    'https://i.ytimg.com/vi/uAh6HWtvbGI/maxresdefault.jpg',
    'https://cdn-photo.pivol.com/15648/imgs/230620211739439264904.jpg',
    'https://im0-tub-ru.yandex.net/i?id=722cbbbda2969b24c54062eafb4627dd-l&n=13',
    'https://img.utdstc.com/screen/423/ca1/423ca108635c5aa691270a23cd99503c73221a9de3077b74ac6eea4245aedcda:200',
    'https://im0-tub-ru.yandex.net/i?id=7d20d6e98eccd69581de02b344c9c6a3-sr&n=13',
    'https://pp.userapi.com/c305703/u183731614/a_53c5c914.jpg?ava=1',
    'https://im0-tub-ru.yandex.net/i?id=55b43ec0f6cbb96bee69602d6df9882b-sr&n=13',
    'https://i.ytimg.com/vi/aQ4J2tiiOso/maxresdefault.jpg',
    'https://sun1-15.userapi.com/impg/c855032/v855032058/235bcf/_OOmbQupw4Y.jpg?size=200x0&quality=88&crop=0,304,1344,1344&sign=ca4151a808513a8a18abd6df5e3efc4a&c_uniq_tag=llX9k25qth-YV-DyFbkrc0dVp8m9amXWLhAZIEM3MWY&ava=1',
    'https://i.ytimg.com/vi/P8RimxG2lYc/maxresdefault.jpg',
    'https://i.ytimg.com/vi/d-KF3x5kIao/maxresdefault.jpg',
    'https://scx2.b-cdn.net/gfx/news/hires/2016/takingandsha.jpg',
    'https://i.ytimg.com/vi/21lgAJiXEPQ/maxresdefault.jpg',
    'https://atn.ua/sites/default/files/1869749.jpg',
    'https://im0-tub-ru.yandex.net/i?id=05c667036f20a5311f6c2e7aa19207c8-l&n=13',
    'https://i.ytimg.com/vi/MaDQSF_HGRQ/maxresdefault.jpg',
    'https://sun9-4.userapi.com/c205816/v205816566/66741/q1dBJpowxtc.jpg?ava=1',
    'https://im0-tub-ru.yandex.net/i?id=86a2fb53a963c1140622f49fc5b3ee12-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=7c5832b523d5269dd1016bb6e12480c4-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=040af5ce70fb8d6bc97650fa00d7d467-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=676e1a5939e422d5497cc4daeff223be-l&n=13',
    'https://sun9-19.userapi.com/impf/c837629/v837629658/1ca8a/9O-SY-W9kZc.jpg?size=453x604&quality=96&sign=05eed34c6c6a86b2451792fe507a2cfa&c_uniq_tag=dVNXz4-gwuFQNT9vY-_AZFl5pv9gTeyBVDuy6rEK-6c&type=album',
    'https://cdni.ilikeyou.com/ui_big/2216949.jpg',
    'https://sun6-21.userapi.com/s/v1/if1/FSvhXDqNleCyfkZTDWYhJm2Sf5L4U4PkvwH1EcHboNQJng-4x4cQVYTMyPWsZLMIIeyL1Q.jpg?size=200x0&quality=96&crop=0,472,1215,1215&ava=1',
    'https://im0-tub-ru.yandex.net/i?id=b7c784e9e68816b1a514d166ae2c1495-l&n=13',
    'https://pbs.twimg.com/media/DKAZv4JWkAAPzuM.jpg:large',
    'https://sun9-25.userapi.com/impg/c854220/v854220693/1f37cb/sUB1yl2c4Y0.jpg?size=320x427&quality=96&sign=c7d84f32b11fabc194bcbaaddd88a053&c_uniq_tag=_E6sbWUNbebU81seI24nhOKUxBt9KveY-SkLE_eFtuo&type=album',
    'https://pbs.twimg.com/media/E4UbAZWUUAEWN8c.jpg',
    'https://i.ytimg.com/vi/9MIC3VzEOvI/maxresdefault.jpg',
    'https://im0-tub-ru.yandex.net/i?id=23eec5063fefdb0391d914a2858e676b-l&n=13',
    'https://sun9-22.userapi.com/Fqt3OKOu5z2KZ2jNnVcOOJ0WkPsn91gtgbTRfQ/sKgggyIB1NY.jpg',
    'https://sun9-80.userapi.com/impg/gB_Ax3i5VlGbCXVGYl5Tr42Hvd1Bw1dn4hdTcg/N4ue6RkgexI.jpg?size=130x260&quality=96&sign=1a16e5ef83907038096d1744176b51c1&type=album',
    'https://im0-tub-ru.yandex.net/i?id=e610dbb0351dc3c6cfef1b2da7293e6a-l&n=13',
    'https://maski-instagrama.ru/wp-content/uploads/a/f/8/af8a7ba01af6f656d4a923f3856cfe5d.jpeg',
    'https://r2.mt.ru/r2/photo5D43/20794334004-0/jpeg/bp.jpeg',
    'https://i.ytimg.com/vi/oVqMNjNyS9w/hqdefault.jpg',
    'https://o.aolcdn.com/images/dims?crop=1600%2C1067%2C0%2C0&quality=85&format=jpg&resize=1600%2C1067&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-02%2Fb78add30-5023-11ea-bffb-0953dcaf00c5&client=a1acac3e1b3290917d92&signature=071ce417b4d9ed177bcbe7dd4479845a6528504c',
    'https://sun1-97.userapi.com/s/v1/ig2/MXwjIvXdwqZPsFqXF_dHClGBfr5vPKkRV6KawDJ6ggI0pQ_A-TnTVaUWGGqkPv4EkTRAru9_CpTFIFfownNSd5Qt.jpg?size=200x266&quality=96&crop=0,0,960,1280&ava=1',
    'https://im0-tub-ru.yandex.net/i?id=823a3f44ce1b46b74c0374f98385840e-l&n=13',
    'https://i.pinimg.com/originals/a7/ba/f4/a7baf40b9e68321e3074c5aa2825d74f.jpg',
    'https://i.ytimg.com/vi/vH3G-zmApYw/hqdefault.jpg',
    'https://i.ytimg.com/vi/yfZak3dYDEw/maxresdefault.jpg',
    'http://www.smartphone.ua/img/arts/7399/ins/1566221108335_.jpg',
    'https://sun6-16.userapi.com/c855620/v855620557/1d3ab5/U8x51d8k1zM.jpg?ava=1',
    'https://sun6-20.userapi.com/s/v1/if1/iwrpf3USkojoRLUJCUjAkmxccOaGEmW7VQi5W6Nf5kAAnFZTuWCCEVg-rRBWOQ0fl77iPAdx.jpg?size=400x0&quality=96&crop=0,0,480,800&ava=1',
    'https://sun9-49.userapi.com/impg/OhErPyADFu_0ZWMeGq3-iP_uiDr8FtZmluH7SA/cRrijVGH86U.jpg?size=453x604&quality=96&sign=dcb0be4f452fbd8497f796a4bf6e83a9&type=album',
    'https://i.ytimg.com/vi/pWdYpHU1fPg/maxresdefault.jpg',
    'https://i.ytimg.com/vi/0LLo3ZJIR4I/maxresdefault.jpg',
    'https://avt-13.foto.mail.ru/list/gromov7474/_avatar180?1328116795&mrim=1',
    'https://im0-tub-ru.yandex.net/i?id=e789f4b0f66d243a7cd89d40762ee193-l&n=13',
    'https://sun1-88.userapi.com/s/v1/ig2/R1p3l4iD5yeZ9Izt8o6J5SFBm79OdpvCkpjwVJ3lNJ5Ra9fMp4vFRx5WawItvRvx5kUJmz5drtAJ4u7SOYA_WOt-.jpg?size=200x200&quality=96&crop=387,516,275,275&ava=1',
    'https://im0-tub-ru.yandex.net/i?id=d4a3522a3f31a575fcd339a435e87c08-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=7c1438b8459494ec9f9aa770a43a86ef-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=86fd197e4be9e3fa1a6a40316b9ee275-l&n=13',
    'https://sun9-41.userapi.com/impf/c850616/v850616194/7dbc6/G9YKQZDpaCc.jpg?size=320x569&quality=96&sign=cc6667ecab89af44c970aef4b53ac2cb&c_uniq_tag=8oymHh9y_WN78kLRsJAWqzE2h2eCxyoDjKhS896x9Ek&type=album',
    'https://sun9-66.userapi.com/c4437/u132687019/-6/m_68efa479.jpg',
    'https://i.ytimg.com/vi/CsdvRl_UlzU/maxresdefault.jpg',
    'https://sun9-58.userapi.com/impg/TQ_J3RfNiZWH34UdCNIU-QVoQbX1wpagz2mDHw/UNTW5NuQYG4.jpg?size=200x433&quality=96&sign=bca7d2d558e8d92d0a21b2d8749ec16b&c_uniq_tag=2Qkl-6TMT7jtGgo9hR3X0SE4RbF_2636VIU80WBl52Y&type=album',
    'https://im0-tub-ru.yandex.net/i?id=f1407753e2eb74ed2e0c67125b7527a9-sr&n=13',
    'https://pp.userapi.com/c638620/v638620828/4464e/PjHWkNQhIcY.jpg',
    'https://i.ytimg.com/vi/KvQHTU5LDeg/hqdefault.jpg',
    'https://im0-tub-ru.yandex.net/i?id=10463f82abfb0e921d2747d644fa6ff8-l&n=13',
    'https://pbs.twimg.com/media/E-lV_kHX0AIEknD.png',
    'https://im0-tub-ru.yandex.net/i?id=d3d7116d2a05be4806c515da3c7d875a-l&n=13',
    'https://sun9-53.userapi.com/impf/-H7Opi6Hnr_tJIDj0cc5DX5zEyq0J3tmLYjYEg/pPEahkS7gsU.jpg?size=453x604&quality=96&sign=52e0f0c504d13464a441186eddae1445&c_uniq_tag=pYlR8moh6yepgstvBdjw_Eq2NEtC2mT8uJS3dQlqT4c&type=album',
    'https://image.winudf.com/v2/image/Y29tLk1KLk1hbi5IYWlyLlNhbG9uLlBob3RvLkNhbWVyYV9zY3JlZW5fNV8xNTI4NDM1NzMwXzA5Ng/screen-5.jpg?fakeurl=1&type=.jpg',
    'https://sun9-1.userapi.com/c855328/v855328931/69715/6u4jbufrSNU.jpg?ava=1',
    'https://sun1-99.userapi.com/s/v1/ig1/2p9Xuie7ejz9sflHTCBV65p4whxNNXsLn0mZa3dd-gd0lVYIufvmfwRYy62826j_CzDDqszQ.jpg?size=400x0&quality=96&crop=0,160,960,961&ava=1',
    'https://i.ytimg.com/vi/znoiONw9vsY/maxresdefault.jpg',
    'https://im0-tub-ru.yandex.net/i?id=4b29124ecc2b2e5b280df553dc56ff67&n=13',
    'https://cache3.youla.io/files/images/780_780/5b/27/5b278e7ad138b37c3e5e7528.jpg',
    'https://im0-tub-ru.yandex.net/i?id=0b70d05b48d53698b5863262bf4d6b39-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=ade20e42380634201e4c5bbbc200a3ba&n=13',
    'https://pbs.twimg.com/media/DQIYxrjX0AUiVhH.jpg',
    'https://im0-tub-ru.yandex.net/i?id=51ad1d343791406975552f09b7d77c5b-sr&n=13',
    'https://sony-ericsson.ru/img_obzor/1480059/small_sony_xperia_xa_ultra_1504194011_5929.jpg',
    'https://pp.userapi.com/c844216/v844216100/121273/wQOCm7-FWTU.jpg?ava=1',
    'https://i05.fotocdn.net/s122/066fda8e619b03d0/gallery_s/2801113647.jpg',
    'https://pp.userapi.com/c637828/v637828412/49f14/Uqyc9eoGrq8.jpg?ava=1',
    'https://pbs.twimg.com/amplify_video_thumb/1135404625010446336/img/ZRRP9iX9bvX4rQAE.jpg',
    'https://sun1-94.userapi.com/s/v1/if1/qa-v6nhnmJWdYdsqL59StykEbLo_oKxWbd6TBPB0jVpDHXFoNNeESZ5oO5d9dMw2QtpYgltb.jpg?size=400x0&quality=96&crop=0,277,1216,1216&ava=1',
    'https://i.ytimg.com/vi/EoYsG3bz8rg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAr0R2gw03DkGXK8deeoc7VBIHvbQ',
    'https://71.img.avito.st/432x324/5726192671.jpg',
    'https://sun9-80.userapi.com/s/v1/ig1/4q2gzGYoWbdhCKfdGjYB4Yf11MSpK6OrUv-kuCO4OQOIaKRVgmV3Vtd2-zs89x9Q-1n3k-sw.jpg?size=200x200&quality=96&crop=25,14,581,581&ava=1',
    'https://im0-tub-ru.yandex.net/i?id=11c1add090e5994b789d63f40a4fb70c-l&n=13',
    'https://s00.yaplakal.com/pics/pics_original/3/2/7/15942723.jpg',
    'https://im0-tub-ru.yandex.net/i?id=5ad6ac1b504c23f4cbb9d6e79c275b0f-l&n=13',
    'https://sun9-31.userapi.com/c5282/u156661717/-14/x_faf061ce.jpg',
    'https://sun9-28.userapi.com/impf/c638620/v638620828/4464f/0_izmAXEpKg.jpg?size=320x569&quality=96&sign=4665387a75ac8e6eaf63bc00b029a6ec&c_uniq_tag=XzuMXJnQJk0CTNBIP4mgDL47llGkTzh5wPV9cXDg3kQ&type=album',
    'https://pbs.twimg.com/media/DOrLWp6W4AAobBK.jpg',
    'https://im0-tub-ru.yandex.net/i?id=5fe658bca6f47796cd9714caad328956-l&n=13',
    'https://i.ytimg.com/vi/Ysypkliio1Y/hqdefault.jpg',
    'https://i.ytimg.com/vi/1nEZo1iCQGQ/maxresdefault.jpg',
    'https://pbs.twimg.com/media/E-btbkvVQAQ_qCB.jpg',
    'https://pbs.twimg.com/media/EW2nihmU0AEESgm.jpg',
    'https://im0-tub-ru.yandex.net/i?id=241ce40d15d52b3b7c35f275c000d613-l&n=13',
    'https://sun6-21.userapi.com/s/v1/if1/iNq26y1hh_zau8nEYCHDZ3Arro9uXEJL1QM7ggSQ3ViqwwbMTn_YrvStOOU0wwU4uTGqOtjz.jpg?size=200x0&quality=96&crop=0,243,720,720&ava=1',
    'https://sun9-2.userapi.com/c845021/v845021497/1acc1e/8fS-E7nuqJ8.jpg',
    'https://en.islcollective.com/preview/job/201907/f/get-paid-to-chat-with-people-tutor-with-cambly-2f71aa_2951_1.jpg',
    'https://pbs.twimg.com/media/EQf-JR8WkAMrGS9.png',
    'https://sun9-34.userapi.com/c830108/v830108094/1b3db9/tRZqF6yvans.jpg',
    'https://sun9-42.userapi.com/impf/c623118/v623118048/8a94/BbZMDroh7xQ.jpg?size=320x480&quality=96&sign=e4c546110aadd0de855577f79326c2db&c_uniq_tag=NF1ew6oskM_NW0TCYA0iA2j8Gn7WeqxB-w09H2vlYs4&type=album',
    'https://im0-tub-ru.yandex.net/i?id=2973b3eceb90e157fe25f552944dc6da-l&n=13',
    'https://pbs.twimg.com/media/EWICpKbU0AELcZL.jpg',
    'https://im0-tub-ru.yandex.net/i?id=5afc1b36795f672bfb16588853fa3a2d-l&n=13',
    'https://im0-tub-ru.yandex.net/i?id=d07bbd62b6ca0892e2ec425a5b27d24e-l&n=13',
    'https://sun9-12.userapi.com/impf/c604727/v604727213/2d04d/6cn76o-1-1c.jpg?size=320x427&quality=96&sign=3eaddb4c68b136a4f7478f6e91083210&c_uniq_tag=5jRJDHt8RID10bU0rTDwiONMJVMI_1MGNXJ4WVuwXoI&type=album',
    'https://im0-tub-ru.yandex.net/i?id=e184394e6eba72719ebb82644692b795-l&n=13',
    'https://ukranews.com/upload/img/2019/02/07/5c5c111c2e6b4------------------.png',
    'https://cdn.mobilesyrup.com/wp-content/uploads/2017/07/snap-chat-rbc-canada-day.jpg',
    'https://pp.userapi.com/c836630/v836630996/4e090/s7MdcsjDKo8.jpg?ava=1',
]
image_urls = list(set(image_urls))

SAVE_PATH = 'D://datasets/spoofing_data'


parser = YParser(
    name='selfie_mobile',
    save_folder=SAVE_PATH,
    download_workers=16,
    parser_workers=3,
    limits=[20, 20],
    wandb_log=False,
)
parser.parse(links=image_urls)
