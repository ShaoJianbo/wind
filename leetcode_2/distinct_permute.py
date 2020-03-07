class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        used = [False] * len(nums)
        res = []

        def backtrack(nums, start, pre, used, res):
            if start == len(nums):
                res.append(pre.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                        continue
                    used[i] = True
                    pre.append(nums[i])
                    backtrack(nums, start + 1, pre, used, res)
                    used[i] = False
                    pre.pop()

        pre = []
        backtrack(nums, 0, pre, used, res)
        return res

    def permute_all(self, nums):
        if not nums:
            return []
        res = []
        def backtrack(nums, start):
            if start == len(nums):
                res.append(list(nums))

            for i in range(start,len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(nums, start+1)
                nums[i], nums[start] = nums[start], nums[i]
        backtrack(nums,0)
        return res


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 2, 2]
    res = so.permuteUnique(nums)
    print(res)
    nums = [1, 2, 3]
    res = so.permute_all(nums)
    print(res)