from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(f"A {nums}")
        muti = nums[0]
        need = nums[0]
        muti_flag = False
        need_flag = False
        # 查找重复的数
        for i in range(len(nums)):
            # 查找需要的数
            if i + 1 not in nums and not need_flag:
                need = i + 1
                need_flag = True
            if i + 1 < len(nums) and nums[i] == nums[i + 1] and not muti_flag:
                muti = nums[i]
                muti_flag = True
        return [muti, need]


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 2, 4]
    nums = [1, 1]
    nums = [3, 2, 3, 4, 6, 5]
    res = so.findErrorNums(nums)
    print(res)
