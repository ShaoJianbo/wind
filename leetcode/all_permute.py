# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = []
#         n = len(nums)
#
#         def backtrack(nums, start):
#             print("start==>", start, "nums", nums)
#             if start == len(nums):
#                 print("OK")
#                 ans.append(list(nums))
#             for i in range(start, len(nums)):
#                 nums[start], nums[i] = nums[i], nums[start]
#                 backtrack(nums, start + 1)
#                 nums[start], nums[i] = nums[i], nums[start]
#         backtrack(nums, 0)
#         return ans


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global ans
        ans = []

        def backtrack(nums, start=0):
            if start == len(nums):
                ans.append(list(nums))
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(nums, 0)
        return ans


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3]
    res = so.permute(nums)
    print(res)
