import benchmark


@benchmark.time
def add(x, y):
    z = x + y
    return z


add(2, 3)
