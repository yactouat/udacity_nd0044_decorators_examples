from functools import wraps
import time


def tracer(func):
    '''decorator that traces the execution time of a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # printing the string representation of the func name
        print(f"{func.__name__!r} run in {run_time:.4f} seconds")
        return value
    return wrapper


@tracer
def some_calculation(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])


some_calculation(10)
