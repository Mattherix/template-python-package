"""The file that manage logger inside the package"""
import logging
from logging.handlers import RotatingFileHandler
import os
from .debug import DEBUG

HERE = os.path.abspath(os.path.dirname(__file__))

LOG_PATH = HERE + '/log/'

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


def init_logger(filename, log_path=LOG_PATH):
    """This create a logger inside your log path.

    This create a log file inside your log path a an Logger object to use it.
    You will want to use this function to log everything than happen in your file.


    :param filename: The name of the file
    :type filename: str
    :param log_path: The path where to put the log file
    :type log_path: str
    :return: A logger
    :rtype: Logger
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    if DEBUG:
        # In debug mode we log inside file
        if filename not in os.listdir(log_path):
            # The file doesn't exist
            with open(log_path + filename, 'w'):
                pass
        file_handler = RotatingFileHandler(log_path + filename, 'a', 10000000, 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    return logger
