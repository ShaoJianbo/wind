from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     dp = [n for n in nums]
    #     # dp[i+1] = max(dp[i], dp[i-1]+nums[i+1])
    #     for i in range(1, len(nums)):
    #         dp[i] = max(dp[i - 1], dp[i])
    #         if i >= 2:
    #             dp[i] = max(dp[i], dp[i - 2] + nums[i])
    #     print("dp->{0}".format(dp))
    #     return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if not nums or nums == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[0:len(nums) - 1]
        print("nums->", nums, "nums1->", nums1, "nums2->", nums2)
        dp1 = [n for n in nums1]
        dp2 = [n for n in nums2]
        print("dp1->", dp1)
        print("dp2->", dp2)
        for i in range(1, len(nums1)):
            dp1[i] = max(dp1[i - 1], nums1[i])
            if i >= 2:
                dp1[i] = max(dp1[i], dp1[i - 2] + nums1[i])

        for i in range(1, len(nums2)):
            dp2[i] = max(dp2[i - 1], nums2[i])
            if i >= 2:
                dp2[i] = max(dp2[i], dp2[i - 2] + nums2[i])

        print("dp1->{0}".format(dp1))
        print("dp2->{0}".format(dp2))

        return max(dp1[-1], dp2[-1])


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    # # nums = [0]
    # # nums = [1]
    # # nums = [1, 2]
    # # nums = [1, 2, 1, 1]
    # # nums = [2, 3, 2]
    res = so.rob(nums)
    print(res)
