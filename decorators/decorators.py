# from https://realpython.com/primer-on-python-decorators

import functools
import time


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


@debug
def repeat(_func=None, *, num_times=2):
    @debug
    def decorator_repeat(func):
        @debug
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            rv_list = list()
            for _ in range(num_times):
                rv = func(*args, **kwargs)
                rv_list.append(rv)
            return rv_list

        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def countcalls(func):
    num_calls = 0

    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Call {num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    return wrapper_count_calls


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
