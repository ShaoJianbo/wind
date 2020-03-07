from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.quick_jump(nums)

    def jump_step(self, nums, start):
        """从start开始检查能否跳跃到最后一个位置"""
        # print("start->{0}".format(start))
        next_step = nums[start]
        if start >= len(nums) - 1:
            return True
        if start + next_step >= len(nums) - 1:
            return True
        if next_step == 0:
            return False

        for i in range(1, next_step + 1):
            print("start==>{0}:{1}".format(start, i))
            can_jump = self.jump_step(nums, start + i)
            if can_jump:
                return True

        return False

    def quick_jump(self, nums):
        """返回从坐标0点开始的"""
        max_step = 0
        for i in range(0, len(nums)):
            # 从0能跳跃的最大步到不了第i步，必然失败
            if max_step < i:
                return False
            if max_step >= len(nums) - 1:
                return True
            max_step = max(max_step, i + nums[i])
        if max_step >= len(nums) - 1:
            return True
        return False


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    nums = [1]
    nums = [2, 0]
    nums = [2, 5, 0, 0]
    # nums = [3, 2, 1, 0, 4]
    # nums = [1, 2, 3]
    nums = [
        2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2,
        6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4,
        6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4,
        3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8,
        2, 2, 7, 5, 1, 7, 9, 6
    ]
    res = so.canJump(nums)
    print(res)
