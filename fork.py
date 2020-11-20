import os as o
import logboot
import logging
import sys
import time

hello = " Hello World!"
logboot.setprefix('P')

logging.info(f"command line args: {sys.argv}")
if len(sys.argv) > 1: me = 'E'

logging.info(f"{o.getpid()} pre-fork")
f_pid = o.fork()
if f_pid == 0: 
    logboot.setprefix('C')

logging.info(f"post-fork forked={f_pid}")
logging.info(f"{hello} parent pid={o.getppid()}")

if f_pid > 0:
    logging.info("waiting for child to terminate")
    result = o.waitpid(f_pid, 0)
    logging.info(f"child terminated, result={result}")
    logging.info("I will terminate")
else:
    logging.info("sleeping")
    time.sleep(2)
    logging.info("woke up")

if len(sys.argv) < 2:
    logging.info("I will now exec")
    o.execl(sys.executable, sys.argv[0], sys.argv[0], "exec")

