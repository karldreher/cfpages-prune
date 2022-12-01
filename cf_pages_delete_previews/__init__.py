import logging
import sys

file_handler = logging.FileHandler(filename='cf_pages_delete_previews' + '.log')
stdout_handler = logging.StreamHandler(sys.stdout)
logging_handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=logging_handlers, format='%(asctime)s %(levelname)s - %(message)s',
                    level='INFO', datefmt='%Y-%m-%d %I:%M:%S %p')
