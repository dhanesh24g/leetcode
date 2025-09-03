def partition(ip: int, max_part: int):
    if ip == 0:
        return 1

    if max_part == 0 or ip < 0:
        return 0

    return partition(ip, max_part - 1) + partition(ip - max_part, max_part)

# print(partition(2, 2))
# print(partition(2, 2))
print(partition(7, 4))
