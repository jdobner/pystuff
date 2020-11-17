import time
import threading
import logboot
import logging
import math
from multiprocessing.pool import Pool
import multiprocessing
from os import getpid
from os import fork


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    iterations = manager.Value('i', 0)


def do_cpu_intesive(num):
    logging.info(f"fork={fork()}")
    threading.currentThread().setName(f"cpu-{num}-{getpid()}")
    i = 10_000_000
    start = time.perf_counter()
    logging.info(f"starting {i} iterations")
    for it in range(i):
        iterations.value += 1
        x = math.cos(99)
        if it % (i / 10) == 0:
            logging.info(f"iteration={it}, global={iterations.value}")
    duration = round(time.perf_counter() - start, 2)
    logging.info(f"done in {duration}")
    return (num, duration)


def do_it_all():
    start = time.perf_counter()
    i = [1, 2]
    with Pool(2) as p:
        results = p.map(do_cpu_intesive, i)

    duration = round(time.perf_counter() - start, 2)
    logging.info(f'Finished in {duration} seconds')
    return results

if __name__ == '__main__':
    do_it_all()


