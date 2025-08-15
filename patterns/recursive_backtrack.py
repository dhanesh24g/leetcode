def subset(nums):

    n = len(nums)
    res = []
    sol = []

    # Recursively call back-track and traverse in_order way
    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return res

        # Do not pick this number
        backtrack(i+1)

        # Pick this number
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

        return res

    backtrack(0)
    return res



def main():
    nums = [1, 2, 3, 4]

    print("nums: ", nums)
    print("subset: ", subset(nums))


if __name__ == "__main__":
    main()
