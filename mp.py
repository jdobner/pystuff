import time
import threading
import logging
import math
from multiprocessing.pool import Pool
import multiprocessing as mp
from multiprocessing.sharedctypes import Value
from os import getpid
import logboot

def do_cpu_intesive(num):
    threading.currentThread().setName(f"cpu-{num}-{getpid()}")
    i = 10_000_000
    start = time.perf_counter()
    logging.info(f"starting {i} iterations")
    block_size = int(i / 10)
    for it in range(1,i+1):
        x = math.cos(99)
        if it % block_size == 0:
            iterations.value = iterations.value + block_size
            logging.info(f"iteration={it:,}  global={iterations.value:,}")
    duration = round(time.perf_counter() - start, 2)
    logging.info(f"done in {duration}")
    return (num, duration)

def init_globals(it):
    global iterations
    iterations = it



def do_it_all():

    start = time.perf_counter()
    i = [1, 2]
    global iterations
    iterations = Value('i', 0)

    with Pool(processes=2, initializer=init_globals, initargs=[iterations]) as p:
        results = p.map(func=do_cpu_intesive, iterable=i)
        
    duration = round(time.perf_counter() - start, 2)
    logging.info(f'Finished in {duration} seconds')
    return results

if __name__ == '__main__':
    do_it_all()


