from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        target_num = 0
        if not nums:
            return target_num
        left = right = 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            while left < right and product >= k:
                product /= nums[left]
                left += 1
            if product < k:
                target_num += (right-left+1)
            right += 1

        return target_num


if __name__ == '__main__':
    so = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    # nums = [1, 2, 3]
    # k = 0
    res = so.numSubarrayProductLessThanK(nums, k)
    print(res)


