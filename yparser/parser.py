import os
import pandas as pd

from yparser.src.downloader.downloader import DownloaderPool
from yparser.src.parser.yandex_parser import YandexParserPool
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
            parse_type='url',
    ):
        if wandb_log:
            import wandb
            wandb.init(project=wandb_project, name=name, reinit=True)
        self.save_path = os.path.join(save_folder, name)
        self.logger = Logger(wandb_log=wandb_log)
        self.logger.setDaemon(True)
        self.logger.start()
        self.dm = DownloaderPool(
            n_workers=download_workers,
            save_folder=self.save_path,
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
        #print('start')
        self.ypm.input_queue.join()
        #print('end parser')
        #print(self.dm.input_queue.qsize())
        if not self.dm.input_queue.empty():
            self.dm.input_queue.join()
        #print('end downloader')
        if not self.logger.queue.empty():
            self.logger.queue.join()
        #print('end logger')
        df1 = pd.DataFrame(self.logger.df)
        df2 = pd.DataFrame(self.logger.save_df)
        df = pd.merge(df1, df2, on='url', how='inner')
        df.to_csv(os.path.join(self.save_path, 'link.csv'), index=False)

