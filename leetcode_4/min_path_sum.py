from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 使用动态规划的方法进行
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        dp = [[float('inf') for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp[i][j] = sum(grid[i][0:j + 1])
                if j == 0:
                    dp[i][j] = sum([grid[k][j] for k in range(i + 1)])

                left = dp[i][j - 1] + grid[i][j] if j > 0 else float('inf')
                top = dp[i - 1][j] + grid[i][j] if i > 0 else float('inf')
                dp[i][j] = min(dp[i][j], left, top)

        print(dp)
        print(dp[row - 1][col - 1])


if __name__ == '__main__':
    so = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    res = so.minPathSum(grid)
    print(res)
