from functools import wraps


def documented_decorator(decorated_function):
    @wraps(decorated_function)
    def wrapper(*args, **kwargs):
        print("printed BEFORE decorated_function is called")
        return decorated_function(*args, **kwargs)
    return wrapper


@documented_decorator
def some_func(some_str_arg):
    '''the introspection information about the original function 
       will be preserved'''
    return f"doing stuff with {some_str_arg}"


help(some_func)
