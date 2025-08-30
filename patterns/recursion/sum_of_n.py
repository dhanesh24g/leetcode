from functools import cache

@cache
def summation(n):

    if n == 0:
        return 0

    return n + summation(n - 1)


print(summation(10))