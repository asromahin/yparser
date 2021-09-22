from yparser.parser import YParser
image_urls = [
    'C:\\Users\\asrom\\Downloads\\Telegram Desktop\\1.jpg',
]
image_urls = list(set(image_urls))

SAVE_PATH = 'D://datasets/test_path'


parser = YParser(
    name='test',
    save_folder=SAVE_PATH,
    download_workers=4,
    parser_workers=1,
    limits=[20, 100],
    wandb_log=False,
    parse_type='path',
)
parser.parse(links=image_urls)
