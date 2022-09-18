from functools import wraps
import logging

import custom_logger


def logger(func):
    '''decorator to log function calls'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("custom_logger")
        logger.debug(f"calling {func.__name__!r}")
        value = func(*args, **kwargs)
        return value
    return wrapper


@logger
def some_func():
    print("I do something")

@logger
def some_func2():
    print("I do something else")

some_func()
some_func2()
