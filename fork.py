import os as o
import logboot
import logging
import sys
import time
from colorama import Fore

hello = " Hello World!"
logboot.config_formatter('P', Fore.YELLOW)

logging.info(f"command line args: {sys.argv}")
if len(sys.argv) > 1: me = 'E'

logging.info(f"{o.getpid()} pre-fork")
f_pid = o.fork()
if f_pid == 0: 
    logboot.config_formatter('C', Fore.GREEN)

logging.info(f"post-fork forked={f_pid}")
logging.info(f"{hello} parent pid={o.getppid()}")

if f_pid > 0:
    logging.info("waiting for child to terminate")
    result = o.waitpid(f_pid, 0)
    logging.info(f"child terminated, result={result}")
    logging.info("I will terminate")

    if len(sys.argv) < 2:
        logging.info("I will now exec")
        o.execl(sys.executable, sys.argv[0], sys.argv[0], "exec")

else:
    logging.info("sleeping")
    time.sleep(.5)
    logging.info("woke up")
