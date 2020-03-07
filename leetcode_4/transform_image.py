from typing import List


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     # 将图像原地旋转90度
    #     # 1.元素行列对换 --> 反转每行
    #     n = len(matrix)
    #     print("0:matrix->", matrix)
    #     for i in range(0, n):
    #         j = i
    #         while 0 <= j < n:
    #             print("i->j", i, j)
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #             j += 1
    #
    #     print("A:matrix->", matrix)
    #     for i in range(0, n):
    #         matrix[i].reverse()
    #     print("B:matrix->", matrix)

    # def rotate(self, matrix: List[List[int]]) -> None:
    #
    #     n = len(matrix)
    #     if n <= 1:
    #         return
    #     else:
    #         for i in range(0, n // 2):
    #             print("i->", i)
    #             self.move(matrix, i, n)
    #
    # def move(self, matrix, start, n):
    #     i = start
    #     for k in range(start, n - start - 1):
    #         j = k
    #         pre = matrix[i][j]
    #         i, j = j, n - i - 1
    #         pre, matrix[i][j] = matrix[i][j], pre
    #
    #         while i != start or k != j:
    #             i, j = j, n - i - 1
    #             pre, matrix[i][j] = matrix[i][j], pre

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # a[i][j] -> a[n-j-1][i]
        # a[n-j-1][i]-> a[n-1-i][n-j-1]
        # a[n-1-i][n-1-j] -> a[n-1-j][i]
        for i in range(0, n//2):
            for j in range(i, n-1-i):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

        print(matrix)


if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    so.rotate(matrix)
    print(matrix)
