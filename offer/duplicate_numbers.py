from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """将数组元素放到其下标位置"""
        for i in range(0, len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return None


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = so.findRepeatNumber(nums)
    print(res)
