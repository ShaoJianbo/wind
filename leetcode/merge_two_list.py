# -*- coding:utf8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num = m + n
        i = m - 1
        j = n - 1
        while num > 0 and i >= 0 and j >= 0:
            max1 = nums1[i]
            max2 = nums2[j]
            if max1 > max2:
                nums1[num - 1] = max1
                i -= 1
            else:
                nums1[num - 1] = max2
                j -= 1
            num -= 1

        while j >= 0:
            nums1[num - 1] = nums2[j]
            j -= 1
            num -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    so = Solution()
    so.merge(nums1, m, nums2, n)
    print(nums1)
    print(nums2)
