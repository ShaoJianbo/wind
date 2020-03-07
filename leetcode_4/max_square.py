from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # dp[i][j][0]->从右边开始的连续1的个数
        # dp[i][j][1]->从下边开始连续1的个数
        dp = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        row = len(grid)
        col = len(grid[0])
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j][0] = dp[i][
                                      j + 1][0] + 1 if j + 1 < col else \
                    grid[i][j]
                    dp[i][j][1] = dp[
                                      i + 1][j][1] + 1 if i + 1 < row else \
                    grid[i][j]

        print("dp->", dp)
        # 计算最大正方形的面积
        order = min(row, col)
        print("order->", order)
        while order >= 0:
            for i in range(0, row - order + 1):
                for j in range(0, col - order + 1):
                    if dp[i][j][0] >= order and \
                       dp[i][j][1] >= order and \
                       dp[i + order - 1][j][0] >= order and \
                       dp[i][j + order - 1][1] >= order:
                        # print("i->j", i, j, "i+order-1", i + order - 1,
                        #       "j+order-1", j + order - 1)
                        # print("order->", order)
                        return order**2

            order -= 1


if __name__ == '__main__':
    so = Solution()
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # grid = [[1, 1, 0, 0]]
    # grid = [[0, 0, 0, 1]]
    # grid = [[0, 1], [1, 1]]
    grid = [[0]]
    # grid = [[1,1],[1,0]]
    # grid = [[1, 1, 0, 0]]
    res = so.largest1BorderedSquare(grid)
    print("res", res)
