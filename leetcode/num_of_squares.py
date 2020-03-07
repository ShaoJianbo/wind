class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in range(0, n + 1)]

        for i in range(1, n + 1):
            j = 1
            while i >= j * j:
                nums[i] = min(nums[i], nums[i-j * j] + 1)
                j += 1
        print(nums)
        return nums[n]


if __name__ == "__main__":
    n = 12
    so = Solution()
    res = so.numSquares(n)
    print(res)
