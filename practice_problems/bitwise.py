# Power of 3
def power_of_3(n) -> bool:

    while n >= 3:
        n = n / 3
        # print(n)

    return n == 1


def main():
    n = 45
    print(f"Is {n} power of 3: ")
    print(power_of_3(n))

if __name__ == "__main__":
    main()