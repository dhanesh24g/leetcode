from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = set()
    path = []

    def process(i, total):
        if i == len(candidates) or total > target:
            return []

        if total == target:
            return res.add(tuple(path[:]))

        path.append(candidates[i])
        process(i, total + candidates[i])
        path.pop()
        process(i + 1, total)

        return res

    process(0, 0)
    return [list(i) for i in res]


def main():
    print(combinationSum([2,3,6,7], 10))


if __name__ == '__main__':
    main()