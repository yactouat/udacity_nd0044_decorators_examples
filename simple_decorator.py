def simple_decorator(decorated_function):
    # this illustrates how decorators wrap a function to add a functionality
    def wrapper():
        print("printed BEFORE decorated_function is called")
        decorated_function()
        print("printed AFTER decorated_function is called")
    return wrapper


def some_func():
    print("doing stuff")


# this is how `some_func`
# becomes actually decorated
# ! try to comment this line and see what happens ;)
some_func = simple_decorator(some_func)


# calling the function
some_func()
