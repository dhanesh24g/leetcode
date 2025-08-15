# string[start:stop:step]

def shortestPalindrome(s: str) -> str:
        index = 0
        temp = ""
        s = s[::-1]
        # s = dcba

        for i, val in enumerate(s):

            if s[i:] == s[i:][::-1]:
                print("s[i:]", s[i:])
                print("s[i:][::-1]", s[i:][::-1])
                if len(temp) < len(s[i:]):
                    print("temp: ", s[i:])
                    temp = s[i:]
                    index = i

        temp = s[:index] + temp + s[:index][::-1]

        return temp


def main():
    # s = "abcd"
    s = "aacecaaa"
    print("Answer: ", shortestPalindrome(s))


if __name__ == "__main__":
    main()