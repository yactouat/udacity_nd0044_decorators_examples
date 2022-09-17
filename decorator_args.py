def decorator_with_args(decorated_function):
    # this is what makes variadic decorators possible
    def wrapper(*args, **kwargs):
        print("printed BEFORE decorated_function is called")
        decorated_function(*args, **kwargs)
        print("printed AFTER decorated_function is called")
    return wrapper


@decorator_with_args
def some_func(some_str_arg):
    print(f"doing stuff with {some_str_arg}")


@decorator_with_args
def some_other_func():
    print("doing stuff with")


some_func("test")
some_other_func()
