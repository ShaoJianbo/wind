# -*- coding:utf8 -*-


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        res = 0
        # import pdb
        # pdb.set_trace()
        for num in nums:
            print("num==>{0}".format(num))
            i = 0
            j = res
            print("{0}->{1}".format(i,j))
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            print("tails==>{0}, num==>{1}".format(tails, num))
            tails[i] = num
            print("res==>{0}".format(res))
            if j == res:
                res += 1
        return res


if __name__ == '__main__':
    so = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    res = so.lengthOfLIS(arr)
    print(res)
