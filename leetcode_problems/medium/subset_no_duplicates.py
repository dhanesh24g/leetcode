def subset(nums):

    nums = sorted(nums)
    n = len(nums)
    res = set()
    sol = []

    # Recursively call back-track and traverse in_order way
    def process(i):
        if i == n:
            # Only if the leaf node is new, then add to res
            res.add(tuple(sol[:]))
            return res

        # Do not pick this number
        process(i+1)

        # Pick this number
        sol.append(nums[i])
        process(i+1)
        sol.pop()
        return res

    process(0)
    return [list(i) for i in res ]



def main():
    nums = [2, 1, 2, 2]

    print("nums: ", nums)
    print("subset: ", subset(nums))


if __name__ == "__main__":
    main()
