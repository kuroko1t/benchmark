import time as ti
from functools import wraps


def time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = ti.time()
        result = func(*args, **kwargs)
        end = ti.time()
        duration = (end - start) * 1000
        print(f"{func.__name__}:{duration:.3f}[ms]")
        return result
    return inner
