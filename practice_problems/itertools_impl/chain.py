ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ip1 = [1 ,2, 3, 4]
ip2 = ['a', 'b', 'c']

from itertools import chain

def flatten_single(ip: list):

    flat = chain.from_iterable(ip)
    print(list(flat))

flatten_single(ip)

#----------------------------------------#

def merge_multiple_lists(ip1: list, ip2: list):

    merged = chain(ip1, ip2)
    print(list(merged))

merge_multiple_lists(ip1, ip2)