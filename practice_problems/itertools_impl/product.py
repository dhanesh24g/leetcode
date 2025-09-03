from itertools import product

ip1 = [1, 2, 3]
ip2 = [4, 5, 6]

def get_product(ip1, ip2):

    res = product(ip1, ip2)

    for val in res:
        print(val)

get_product(ip1, ip2)