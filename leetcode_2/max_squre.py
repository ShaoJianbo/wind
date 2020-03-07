from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        col = len(matrix[0]) + 1
        row = len(matrix) + 1
        dp = [[0 for c in range(col)] for r in range(row)]

        print(dp)
        max_edge = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i - 1][j - 1] == "1":
                    right_top = dp[i - 1][j]
                    left_bottom = dp[i][j - 1]
                    left_top = dp[i - 1][j - 1]
                    print("i->j", left_top, left_bottom, right_top)
                    dp[i][j] = min(right_top, left_bottom, left_top) + 1
                    max_edge = max(max_edge, dp[i][j])
        print(dp)
        return max_edge**2


if __name__ == "__main__":
    so = Solution()
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    matrix = []
    matrix = [["1", "1"], ["1", "1"]]
    res = so.maximalSquare(matrix)
    print(res)
