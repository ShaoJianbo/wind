class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return target
        ans = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j <= len(nums) - 1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return ans


if __name__ == '__main__':
    nums = [0, 4, 3, 0]
    target = 0
    so = Solution()
    res = so.twoSum(nums, target)
    print(res)
