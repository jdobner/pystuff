import time
import threading
import logging
import sys
import math


def config_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)    



def do_sleep(sleep_time):
    logging.info(f"Sleeping {sleep_time} seconds")
    time.sleep(1)
    time.sleep(sleep_time - 1)
    logging.info("done sleeping...")

def do_cpu_intesive():
    i = 100_000_000
    start = time.perf_counter()
    logging.info(f"starting {i} iterations")
    for it in range(i):
        x = math.cos(99)
        if it % (i / 10) == 0:
            logging.info(f"iteration={it}")
    duration = round(time.perf_counter() - start, 2)
    logging.info(f"done in {duration}")


config_logging()
start = time.perf_counter()
threads = []

for x in range(2):
    t = threading.Thread(target=do_cpu_intesive, name=f'cpu-{x}')
    t.start()
    threads.append(t)

for sec in range(1,6):
    t = threading.Thread(target=do_sleep, args=[sec], name=f"slp-{sec}")
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


duration = round(time.perf_counter() - start, 2)
logging.info(f'Finished in {duration} seconds')

