import logging

"""

logger = logging.getLogger('demo')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s')

stream_handler = logging.StreamHandler()   # מסך
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(        # קובץ
    'app.log', encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.info('Application started')
logger.warning('Low disk space')
"""

logger=logging.getLogger()
