from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        if not nums or len(nums) == 0:
            return []

        i = 0
        res = []
        while i < len(nums):
            cur = nums[i]
            # print("i-->", i, "nums->", nums, "cur->", cur)
            while cur != nums[cur - 1]:
                print("Pro->", cur)
                swap_num = nums[cur-1]
                nums[cur-1] = cur
                cur = swap_num
                nums[i] = cur
            #     print("Pro->", "cur->", cur, "nums->", nums)
            # print("cur->", cur, "nums->", nums)
            i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])

        return res


if __name__ == '__main__':
    so = Solution()
    nums = [2, 1]
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = so.findDuplicates(nums)
    print(res)
