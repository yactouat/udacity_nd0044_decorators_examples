from functools import wraps


# a template for decorators
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # this is where you will put custom logic
        # that needs to be run before calling the original function
        value = func(*args, **kwargs)
        # this is where you will put custom logic
        # that needs to be run after calling the original function
        return value
    return wrapper
