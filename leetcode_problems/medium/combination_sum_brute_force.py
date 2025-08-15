from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    nums = sorted(candidates)
    n = len(nums)
    res = set()
    sol = []

    def process(i, adn):
        if i == n:
            return []

        elif nums[i] > target:
            return []

        elif nums[i] == target:
            return res.add(tuple([nums[i]]))

        else:
            if (adn + nums[i]) <= target:
                sol.append(nums[i])
                process(i, adn + nums[i])
                sol.pop()

            if sum(sol[:]) == target:
                return res.add(tuple(sol[:]))
            elif sum(sol[:]) > target:
                sol.pop()
            else:
                process(i + 1, adn)

        return res

    process(0, 0)
    return [list(i) for i in res]


def main():
    print(combinationSum([2, 4], 10))


if __name__ == '__main__':
    main()