ip = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from itertools import pairwise

def form_pairs(ip):

    pairs = pairwise(ip)
    print(list(pairs))

form_pairs(ip)