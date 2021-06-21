import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
datefmt='%m/%d/%Y %H:%M:%S')


logging.debug('this is debug message')
logging.info('this is info message')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')

import helper