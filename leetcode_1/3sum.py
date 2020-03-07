class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        ans = []
        i = 0
        while i < size - 1:
            j = i + 1
            k = size - 1
            data = -nums[i]
            while j < k:
                if nums[j] + nums[k] == data:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < size - 2 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                else:
                    if nums[j] + nums[k] < data:
                        j += 1
                    else:
                        k -= 1
            while i < size - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans


if __name__ == '__main__':
    so = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-2, 0, 1, 1, 2]
    # nums = [-2,0,0,2,2]
    # nums = [0,0,0]
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 0, 2, 2]
    ans = so.threeSum(nums)
    print("ans-->", ans)
