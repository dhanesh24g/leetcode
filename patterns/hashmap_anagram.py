from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = {}

        for i, val in enumerate(nums2):
            tab[val] = i

        for i, val in enumerate(nums1):
            nums1[i] = tab[val]

        return nums1


if __name__ == "__main__":
    sol = Solution()
    print(sol.anagramMappings([1, 3, 5, 7, 1], [3, 1, 5, 1, 7]))