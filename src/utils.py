# -----------------------------------------------------------
# Python Utils Implementation
# Licensed under The MIT License [see LICENSE for details]
# Written by Cheng-Bin Jin
# Email: sbkim0407@gmail.com
# ------------------------------------------------------------
import os
import logging

logger = logging.getLogger(__name__)  # logger
logger.setLevel(logging.INFO)


def init_logger(log_dir, name, is_train):
    logger = logging.getLogger(__name__)  # logger
    logger.setLevel(logging.INFO)

    file_handler, stream_handler = None, None
    if is_train:
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

        # file handler
        file_handler = logging.FileHandler(os.path.join(log_dir, name + '.log'))
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)

        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # add handlers
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger, file_handler, stream_handler


def release_handles(logger, file_handler, stream_handler):
    file_handler.close()
    stream_handler.close()
    logger.removeHandler(file_handler)
    logger.removeHandler(stream_handler)