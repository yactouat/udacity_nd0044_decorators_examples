def prettier_decorator(decorated_function):
    def wrapper():
        print("printed BEFORE decorated_function is called")
        decorated_function()
        print("printed AFTER decorated_function is called")
    return wrapper


# this way of wrapping a function does the same thing than =>
# some_func = prettier_decorator(some_func)
@prettier_decorator
def some_func():
    print("doing stuff")


some_func()
