ip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

from itertools import accumulate

def running_sum(ip: list):

    total = accumulate(ip)
    print(list(total))

running_sum(ip)