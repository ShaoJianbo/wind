from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        print(nums)
        sort_nums = sorted(nums)
        print(sort_nums)
        i = 0
        j = len(nums) - 1
        k = 0
        while i < len(nums):
            while i< len(nums) and nums[i] != sort_nums[i]:
                print("i-->", i)
                j = min(j, i)
                k = max(k, i)
                i += 1
            i += 1

        print("j-->k", j, k)
        if j == len(nums) - 1 and k == 0:
            return 0
        return k - j + 1


if __name__ == '__main__':
    so = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 2, 3, 4]
    nums = [2, 1]
    res = so.findUnsortedSubarray(nums)
    print(res)
