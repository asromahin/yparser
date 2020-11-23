import os
from yparser import chromedriver
import sys, stat


if 'win' in sys.platform:
    CHROMEDRIVER_PATH = os.path.sep.join(os.path.abspath(chromedriver.__file__).split(os.path.sep)[:-1] + ['chromedriver.exe'])
else:
    CHROMEDRIVER_PATH = os.path.sep.join(
        os.path.abspath(chromedriver.__file__).split(os.path.sep)[:-1] + ['chromedriver']
    )
    os.chmod(CHROMEDRIVER_PATH, stat.S_IRWXO)