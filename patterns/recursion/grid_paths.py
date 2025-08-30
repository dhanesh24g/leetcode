from functools import cache

@cache
def grid_paths(n: int, m: int):

    if n == 1 or m == 1:
        return 1

    return grid_paths(n, m - 1) + grid_paths(n - 1, m)


print(grid_paths(13, 17))
