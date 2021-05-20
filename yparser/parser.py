import wandb
import os

from src.downloader.downloader import DownloaderPool
from src.parser.yandex_parser import YandexParserPool
from src.logger.logger import Logger


class YParser:
    def __init__(
            self,
            name,
            save_folder,
            download_workers=32,
            parser_workers=4,
            limits=[200],
            wandb_log=False,
            wandb_project='yparser',
            parse_type='url',
    ):
        if wandb_log:
            wandb.init(project=wandb_project, name=name, reinit=True)
        save_path = os.path.join(save_folder, name)
        self.logger = Logger(wandb_log=wandb_log)
        self.logger.setDaemon(True)
        self.logger.start()
        self.dm = DownloaderPool(
            n_workers=download_workers,
            save_folder=save_path,
            logger_queue=self.logger.queue,
        )
        self.ypm = YandexParserPool(
            n_workers=parser_workers,
            limits=limits,
            logger_queue=self.logger.queue,
            output_queue=self.dm.input_queue,
            parse_type=parse_type,
        )

    def parse(self, links):
        self.ypm.parse(links=links)
        self.ypm.input_queue.join()
        self.dm.input_queue.join()
        self.logger.queue.join()

