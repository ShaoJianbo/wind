from typing import List


class Solution:
    def findMaxForm(self, arr: List[str], m: int, n: int) -> int:
        """贪心算法:先尝试构建最短的字符串"""
        # 定义一组数组,dp[i][j]表示消耗i个0和j个1构建出来的最长字符串数
        # dp(i, j) = max(1 + dp(i - cost_zero[k], j - cost_one[k]))
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        arr.sort(key=lambda x: len(x))
        cnt = []
        for i, s in enumerate(arr):
            cnt_0 = s.count("0")
            cnt_1 = s.count("1")
            cnt.append([cnt_0, cnt_1])
            for j in range(m, cnt[i][0] - 1, -1):
                for k in range(n, cnt[i][1] - 1, -1):
                    # print(f"{j},{k}-->{cnt[i]}")
                    dp[j][k] = max(1 + dp[j - cnt[i][0]][k - cnt[i][1]], dp[j][k])

        # print(dp)

        return dp[m][n]


if __name__ == '__main__':
    so = Solution()
    arr = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    res = so.findMaxForm(arr, m, n)
    print(res)
