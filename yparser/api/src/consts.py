import os
from yparser import chromedriver

CHROMEDRIVER_PATH = path = os.path.sep.join(os.path.abspath(chromedriver.__file__).split(os.path.sep)[:-1] + ['chromedriver'])