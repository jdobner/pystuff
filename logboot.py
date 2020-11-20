import logging
from logging import Handler
import sys

format = '%(asctime)s - %(process)d - %(threadName)s - %(message)s'


def __config_logging():
    root = logging.getLogger()
    if len(root.handlers) > 0:
        print("pass")
        return

    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(format))
    root.addHandler(handler)    
    root.info("logging configured!")

def setprefix(prefix):
    root = logging.getLogger()
    handler = root.handlers[0]
    handler.setFormatter(logging.Formatter(prefix + " " + format))

__config_logging()



