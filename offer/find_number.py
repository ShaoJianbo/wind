from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 针对每一行进行二分查找
        for nums in matrix:
            res = self.find_target(nums, target)
            if res:
                return True
        return False

    def find_target(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            print(left, right)
            mid = (right + left) // 2
            print("mid->", mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return True

        return False

    def find_target_n(self, matrix, target):
        """
        充分利用给定条件:
        1.每行元素从左到右不断增大
        2.每列元素从上到下不断增大
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return False
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            print(f"{i}->{j}", matrix[i][j])
            # breakpoint()
            if i >= 0 and j < col and target == matrix[i][j]:
                return True
            while i >= 0 and j < col - 1 and target > matrix[i][j]:
                j += 1
            while i >= 0 and j <= col - 1 and target < matrix[i][j]:
                i -= 1
            if i >= 0 and j < col and target == matrix[i][j]:
                return True
        return False


if __name__ == '__main__':
    so = Solution()
    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
    #           [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

    target = 20

    matrix = [[-5]]
    target = -10
    # res = so.searchMatrix(matrix, target)
    res = so.find_target_n(matrix, target)
    print(res)
