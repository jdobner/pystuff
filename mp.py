import time
import threading
import logging
import sys
import math
from multiprocessing.pool import Pool


def config_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)    


def do_cpu_intesive(i):
    threading.currentThread().setName(f"cpu-{i}")
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

if __name__ == '__main__':

    start = time.perf_counter()
    i = [1, 2]
    p = Pool()

    for i in range(2):
        p.apply_async(do_cpu_intesive, [i])

    p.close()
    p.join()

    duration = round(time.perf_counter() - start, 2)
    logging.info(f'Finished in {duration} seconds')




