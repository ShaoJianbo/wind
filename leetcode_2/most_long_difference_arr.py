from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for n in arr:
            dp[n] = dp.get(n - difference, 0) + 1
        return max(dp.values())


if __name__ == '__main__':
    so = Solution()
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference = -2
    res = so.longestSubsequence(arr, difference)
    print(res)