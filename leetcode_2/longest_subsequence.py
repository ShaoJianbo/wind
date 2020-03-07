# -*- coding:utf8 -*-


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 0
        lis_arr = [1] * len(nums)  # 保存最长子序列的最大长度
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    lis_arr[i] = max(lis_arr[i], lis_arr[j] + 1)
            max_len = max(max_len, lis_arr[i])
        return max_len


if __name__ == '__main__':
    so = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    res = so.lengthOfLIS(arr)
    print(res)
