from typing import List
import functools


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums_str = [str(x) for x in nums]
        print(f"{nums_str}")
        nums_str.sort(key=functools.cmp_to_key(self.sort_rule))
        print(nums_str)
        return ''.join(nums_str)

    def sort_rule(self, x, y):
        """排序函数"""
        a = int(x + y)
        b = int(y + x)
        return 1 if a > b else -1


if __name__ == '__main__':
    so = Solution()
    nums = [3, 30, 34, 5, 9]
    res = so.minNumber(nums)
    print(res)
