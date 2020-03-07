from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        if not A:
            return 0
        max_width = 0
        arr = []
        for i, n in enumerate(A):
            arr.append([n, i])
        arr = sorted(arr, key=lambda n: n[0])
        m = float('inf')
        for value, index in arr:
            max_width = max(index - m, max_width)
            m = min(m, index)
        return max_width


if __name__ == '__main__':
    A = [6, 0, 8, 2, 1, 5]
    A = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    so = Solution()
    res = so.maxWidthRamp(A)
    print(res)
