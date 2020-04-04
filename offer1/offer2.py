from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """利用动态规划设计路径"""
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                # print(f"{i}->{j}")
                if i == 0:
                    dp[i][j] = sum(grid[i][0:j+1])
                elif j == 0:
                    dp[i][j] = sum([grid[k][0] for k in range(i+1)])
                elif i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
                # print(f"{i}->{j}={dp[i][j]}")
        # print(f"dp-->{dp}")
        return dp[row - 1][col - 1]


if __name__ == '__main__':
    so = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = so.maxValue(grid)
    print(res)