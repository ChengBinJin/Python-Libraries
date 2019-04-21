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


def init_logger(log_path, name):
	formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
	# file handler
	file_handler = logging.FileHandler(os.path.join(log_path, name))
	file_handler.setFormatter(formatter)
	file_handler.setLevel(logging.INFO)
	# stream handler
	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)
	# add hanlders
	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)
