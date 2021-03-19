import wandb
import os

from yparser.src.downloader.downloader import DownloaderManager
from yparser.src.parser.yandex_parser import YandexParserManager
from yparser.src.logger.logger import Logger


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
    ):
        if wandb_log:
            wandb.init(project=wandb_project, name=name, reinit=True)
        save_path = os.path.join(save_folder, name)
        self.logger = Logger(wandb_log=wandb_log)
        self.logger.setDaemon(True)
        self.logger.start()
        self.dm = DownloaderManager(save_path, n_workers=download_workers, logger=self.logger)
        self.ypm = YandexParserManager(self.dm, n_workers=parser_workers, limits=limits, logger=self.logger)

    def parse(self, links):
        self.ypm.parse(links=links)

