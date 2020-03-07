from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        cnt = left = 0
        right = 0
        product = 1
        while right < len(nums):
            product *= nums[right]
            while product >= k and left <= right <len(nums):
                product /= nums[left]
                left += 1
            cnt += (right - left + 1)
            right += 1

        return cnt

if __name__ == '__main__':
    so = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    # nums = [1, 1, 1]
    # k = 2
    nums = [1,2,3]
    k = 0
    res = so.numSubarrayProductLessThanK(nums, k)
    print(res)
