class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        size = len(nums)
        max_num = 0
        while right < size:
            while right < size and nums[right]:
                right += 1
            max_num = max(max_num, right - left)
            right += 1
            left = right
        return max_num


if __name__ == '__main__':
    so = Solution()
    nums = [1,1,0,1,1,1]
    res = so.findMaxConsecutiveOnes(nums)
    print(res)
