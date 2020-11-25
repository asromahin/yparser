from api.paralel_parser import parse_paralel_by_images_urls
from api.parser import parse_by_images_urls
import time

image_urls = [
'https://ubratdoma.ru/wp-content/uploads/2019/03/kak-podklyuchit-varochnuyu-panel-i-duhovoj-shkaf-k-odnoj-rozetke.jpg',
'https://elsi.by/wp-content/uploads/2019/02/o23.jpg',
'https://lh3.googleusercontent.com/proxy/iWW0SyY-Yh1QSLpjdATznJse7qVHxRJwcxc6zYuIvgEYG4L0Xa2YqUYfJRP4798Jk5BvBrzboA9SUNi_mT1qn25gWNHjiV_9Hd4nYH6uQWddQL-i-nUCwGR25spTapAljrvMPoHw2lbg947lts6APQSt1w',
'https://lh3.googleusercontent.com/proxy/0hRTRISxNbBAKvI8UKI1Ibt-UAjxlb5xYuBNzXKMDi7WhjZbH4HHHAuVe1GR9atX8EaLrwIfQRXjlKbki85r7E1SegzpSZNIVOEnEoDA',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUtwfxK3c816DwlReYZcy4wDD8ZsYuyoTyRA&usqp=CAU',
'https://obustroeno.com/wp-content/uploads/sobrat-prosteyshuyu-tumbochku-pod-varochnuyu-panel-i-duhovku-ne.jpg',
'https://cache3.youla.io/files/images/720_720_out/5b/83/5b83fd462aecd62de9149332.jpg',
'https://lh3.googleusercontent.com/proxy/9AgAlNKvwHBs8sYlddt-FmI66cmmhIMiHYQPlC6pQ4XdFd253xHvm7sIQPkgSRtz7pypurMubUyf9rOsgo2KLR6a05qjF-EepNp3fhv7r59OfybxY8UhUtpgAKmW71vmcWUu32ahncSh-J-pniRpv1-DK1bgncuAy3fTvMaYkup5igf5zfWPxFZSgPCiPR-EaSA869tamYIRHYJX',
'https://s.sakh.com/i/b/market/2016/04/06/35c64bdab7dd0582b7df92200e5e5a84.jpeg',
'https://shkaf-info.ru/wp-content/uploads/2018/11/rozetka-pod-vstrduhovku.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbvfAwDFV498SfA-B5ZkRH6SckjF9GK05ciA&usqp=CAU',
'https://avatars.mds.yandex.net/get-altay/1608507/2a000001682e8c4fbd715f11bd5858b4c607/XXL',
'https://shkaf-info.ru/wp-content/uploads/2018/11/kak-pravilno-vstroit-duhovoy-shkaf-v-penal.jpg',
'https://kuhni-natali.ru/images/ustanovka-vstraivaemoj-tehniki.jpg',
'https://vse-elektrichestvo.ru/wp-content/uploads/2015/11/%D0%A0%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D1%83%D1%85%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%88%D0%BA%D0%B0%D1%84%D0%B0-%D0%B2-%D0%BD%D0%B8%D1%88%D0%B5.png',
'https://sovet-ingenera.com/wp-content/uploads/2019/07/podklyuchenie_gaz_duhovki_10.jpg',
'https://220v.guru/images/673548/ustanovka_elektricheskogo.jpg',
'https://stroy-podskazka.ru/images/article/orig/2019/03/podklyuchenie-duhovogo-shkafa-i-varochnoj-paneli-k-elektroseti-26.jpg',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7keSrtoOJe1eosERzl1xND_50YgBtGZ6UPA&usqp=CAU',
'https://katlovan.ru/800/600/http/mebeltrends.ru/wp-content/uploads/2016/01/ustanovka-duhovogo-shkafa-v-nishu.jpg',
]

parse_paralel_by_images_urls(
    image_urls=image_urls,
    save_path='../data',
    paralel_threads=2,
    n_threads=32,
    limit=500,
    chromedriver_path='../tests/chromedriver.exe'
)

