class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

        vows = []
        for char in s:
            if char in vowels:
                vows.append(char)

        if len(vows) < 2:
            return s
        else:
            vows.sort()

        ans = []
        i = 0
        for val in s:
            if val in vowels:
                ans.append(vows[i])
                i += 1
            else:
                ans.append(val)

        return "".join(ans)


def main():
    print(Solution().sortVowels("lEetcOde"))
    print(Solution().sortVowels("aiAoUuEe"))

main()