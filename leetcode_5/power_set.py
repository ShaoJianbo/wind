from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # for k in range(len(nums) + 1):
        #     self.get_backtrack(start=0, size=k, subset=[], ans=ans, nums=nums)
        # return ans
        ans = self.get_mask(nums, ans)
        return ans

    def get_recursion(self, nums):
        """空集的幂集只有空集,每次增加一个元素让其追加到已有幂集的后面"""
        ans = [[]]
        for i in nums:
            print("i-->", i, "ans->", ans)
            ans += [j + [i] for j in ans]
            print("ans-->", ans)
        return ans

    def get_backtrack(self, start, size, subset, ans, nums):
        """第一个参数为索引,第二个参数为当前子集长度"""
        # 当前子集构造完成->加入集合
        if len(subset) == size:
            ans.append(subset[:])
        # 从first到n没次将nums[i]添加到子集中->进行下一次的遍历
        # 删除添加的元素完成回溯
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.get_backtrack(i + 1, size, subset, ans, nums)
            subset.pop()

    def get_mask(self, nums, ans):
        """根据掩码"""
        # 生成所有长度为n的二进制掩码 ->将每个子集都隐射到一个掩吗数
        n = len(nums)
        for i in range(2**n, 2**(n+1)):
            # generate bitmask, from 0..00 -->1..11
            bitmask = bin(i)[3:]
            print(bitmask)
            ans.append([nums[j] for j in range(n) if bitmask[j]=='1'])
        return ans


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3]
    ans = so.subsets(nums)
    print(ans)
