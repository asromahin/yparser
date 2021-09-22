from yparser.parser import YParser
from yparser.src.utils.kill_instances import kill_chrome_instances
import pandas as pd
import time

df = pd.read_csv('models_df.csv')


def make_query(row):
  return ' '.join([row['brend'], row['model'], row['year'], 'на улице'])


STEP_SIZE = 120

START_STEP = 3
END_STEP = len(df)//STEP_SIZE+1

for j in range(START_STEP, END_STEP):
    image_urls = []
    kill_chrome_instances()
    time.sleep(2)

    STEP = j

    start_i = STEP * STEP_SIZE
    end_i = min((STEP+1) * STEP_SIZE, len(df))

    print(start_i, end_i, len(df))

    for i in range(start_i, end_i):
        row = df.iloc[i]
        query = make_query(row)
        #print(query)
        image_urls.append(query)

    image_urls = list(set(image_urls))

    SAVE_PATH = 'D://datasets/cars/classifications_small/'

    stepname = str(STEP + 1)

    parser = YParser(
        name=f'models_p{stepname}',
        save_folder=SAVE_PATH,
        download_workers=16,
        parser_workers=3,
        limits=[80],
        wandb_log=False,
        parse_type='text',
    )
    parser.parse(links=image_urls)
