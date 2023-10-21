import logging
import os, sys
from datetime import datetime


LOG_DIR = 'logs'
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_DIR_PATH, exist_ok = True)

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

LOG_FILE_NAME = f'logs_{CURRENT_TIMESTAMP}.log'

LOG_FILE_PATH = os.path.join(LOG_DIR_PATH,LOG_FILE_NAME)

logging.basicConfig(filename = LOG_FILE_PATH,
                    filemode = 'w',
                    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)



