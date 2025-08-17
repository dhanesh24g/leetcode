import math as math

def gcdOfStrings(self, str1: str, str2: str) -> str:

    if str1 + str2 != str2 + str1:
        return ""

    # str[start:stop:step]
    return str2[:math.gcd(len(str1), len(str2))]


def main():
    str1 = "LEE"
    str2 = "TCO"
    print(gcdOfStrings(None, str1, str2))

main()