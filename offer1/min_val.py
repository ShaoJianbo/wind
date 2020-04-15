from typing import List

class Solution:
    def minArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i]>nums[i + 1]:
                return nums[i+1]
        return nums[0]