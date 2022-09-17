def returning_decorator(decorated_function):
    def wrapper(*args, **kwargs):
        print("printed BEFORE decorated_function is called")
        # return the function being called to get whatever it returns
        return decorated_function(*args, **kwargs)
    return wrapper


@returning_decorator
def some_func(some_str_arg):
    return f"doing stuff with {some_str_arg}"


print(some_func("test"))
