# —＊-coding:utf8 -*-


class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # 采用滑动窗口协议
        left = 0
        right = 0
        count = 0
        size = len(arr)
        max_size = 0
        while right < size:
            if arr[right] == 0:
                count += 1
            while count > k:
                if arr[left] == 0:
                    count -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
            right += 1
        return max_size


if __name__ == '__main__':
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    so = Solution()
    res = so.longestOnes(A, K)
    print(res)
