import logging
import multiprocessing
from myimports import testfunc
import logboot
from colorama import Fore


def worker(data, mylist, isFork):
    if isFork:
        logboot.config_formatter("F", Fore.GREEN)
    else:
        logboot.config_formatter("S", Fore.YELLOW)

    logging.info(f'addiing {data}')
    for item in data:
        mylist.append(item)

def run_it(l1, l2, fl, isFork):
    process1 = multiprocessing.Process(target=worker, args=[l1, fl, isFork])
    process2 = multiprocessing.Process(target=worker, args=[l2, fl, isFork])

    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print(fl)

def doWork():
    manager = multiprocessing.Manager()

    input_list_one = ['one', 'two', 'three', 'four', 'five']
    input_list_two = ['six', 'seven', 'eight', 'nine', 'ten']

    multiprocessing.set_start_method("spawn", force=True)
    run_it(input_list_one, input_list_two, manager.list(), False)

    multiprocessing.set_start_method("fork", force="True")
    run_it(input_list_one, input_list_two, manager.list(), True)



if __name__ == '__main__':
    logboot.config_formatter("P", Fore.WHITE)
    doWork()
