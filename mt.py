import time
import threading
import logging

start = time.perf_counter()
    

def do_something(sleep_time):
    thread_name = threading.currentThread().getName()
    print(f"{thread_name}: Sleeping {sleep_time} seconds")
    logging.info("Sleeping {sleep_time} seconds")
    time.sleep(sleep_time)
    print(f"{thread_name}: done sleeping...")


threads = []

for sec in range(1,6):
    t = threading.Thread(target=do_something, args=[sec], name=f"sleep-{sec}")
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'{threading.currentThread().getName()}: Finished in {round(finish - start, 2)} seconds')

