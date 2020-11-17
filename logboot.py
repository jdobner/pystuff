import logging
import sys

def config_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)    
    root.info("logging configured!")

config_logging()

