from datetime import datetime


def runs_only_during_business_hours(func):
    def wrapper():
        # if within reasonable business hours
        if 8 <= datetime.now().hour < 19:
            func()
        else:
            # do nothing
            pass
    return wrapper


def some_func():
    print("doing stuff")


# this is how you would restrict a function to run outside of a given timeframe
some_func = runs_only_during_business_hours(some_func)

some_func()
