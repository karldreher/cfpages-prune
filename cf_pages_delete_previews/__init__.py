__version__ = '1.1.0'

import logging
import sys
import os
log_level = os.getenv('LOG_LEVEL', 'INFO')
file_handler = logging.FileHandler(filename='cfpages-prune' + '.log')
stdout_handler = logging.StreamHandler(sys.stdout)
logging_handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=logging_handlers, format='%(asctime)s %(levelname)s - %(message)s',
                    level=log_level, datefmt='%Y-%m-%d %I:%M:%S %p')
