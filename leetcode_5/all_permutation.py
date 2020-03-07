from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        nums = "".join(nums)
        count = [0]
        res = self.get_kth_permitation(nums, count, "", k)
        return res

    def get_kth_permitation(self, nums, count, permutation, k):
        """找出第k和排列"""
        # print(count)
        if len(permutation) == len(nums):
            count[0] += 1
        if count[0] >= k:
            # print(permutation)
            return permutation
        for i in range(0, len(nums)):
            if nums[i] not in permutation:
                pre_str = f'{permutation}'
                permutation = f'{permutation}{nums[i]}'
                res = self.get_kth_permitation(nums, count, permutation, k)
                permutation = pre_str
                if count[0] >= k:
                    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    so = Solution()
    res = so.getPermutation(3, 5)
    print(res)
