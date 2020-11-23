import logging
from logging import Handler
import sys
from colorama import Style


def __config_logging():
    root = logging.getLogger()
    if len(root.handlers) > 0:
        print("pass")
        return

    root.setLevel(logging.DEBUG)
    config_formatter()
    root.info("logging configured!")


def config_formatter(prefix="", color=None):
    root = logging.getLogger()
    root.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(CustomFormatter(prefix, color))
    root.addHandler(handler)


def none_to_empty(anything):
    if anything:
        return anything
    else:
        return ""


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""
    fmt = '%(asctime)s - %(process)d - %(threadName)s - %(message)s'

    def __init__(self, prefix="", color=None):
        if len(prefix):
            prefix += " "
        if color:
            super().__init__(f'{color}{none_to_empty(prefix)}{CustomFormatter.fmt}{Style.RESET_ALL}')
        else:
            super().__init__(f'{none_to_empty(prefix)}{CustomFormatter.fmt}')


__config_logging()



