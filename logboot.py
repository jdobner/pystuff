import logging
import sys

def config_logging():
    if len(logging.root.handlers) > 0:
        print("pass")
        return

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(process)d - %(threadName)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)    
    root.info("logging configured!")

config_logging()

