n = 12345

from itertools import permutations

def generate_permutations(n: int):

    ip = str(n)

    all_permutations = permutations(ip, len(ip))

    for perm in all_permutations:
        print("".join(perm))

generate_permutations(n)