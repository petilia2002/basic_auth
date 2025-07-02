from functools import wraps


def first_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Call decorator #1")
        return fn(*args, **kwargs)

    return wrapper


def second_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Call decorator #2")
        return fn(*args, **kwargs)

    return wrapper


def third_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Call decorator #3")
        return fn(*args, **kwargs)

    return wrapper


@third_decorator
@second_decorator
@first_decorator
def func():
    print("Hello!")


func()
