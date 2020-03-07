from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        save_max = -99999999
        cur_max = 1
        cnt = left = 0
        right = 0
        while right < len(nums):
            cur_max *= nums[right]
            print("i->", right, cur_max)
            left = right
            while left >= 0 and nums[left]!=0 and cur_max / nums[left] >= cur_max:
                cur_max /= nums[left]
                left -= 1
            save_max = max(save_max, cur_max, nums[right])
            right += 1

        return int(save_max)


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, -2, 4]
    nums = [-2,0,1]
    nums = [0, 2]
    nums = [-2,3,-4]
    res = so.maxProduct(nums)
    print(res)
