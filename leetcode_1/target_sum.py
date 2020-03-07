class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        step = {}

        def dfs(cur, i, step):
            print("i->", i, "cur->", cur)
            if i < len(nums) and (cur, i) not in step:  # 搜索周围节点
                step[(cur, i)] = dfs(cur + nums[i], i + 1, step) + dfs(
                    cur - nums[i], i + 1, step)  # noqa
            print("step[(cur,i)]", step.get(cur, i), "cur->", cur)
            return step.get((cur, i), int(cur == S))

        return dfs(0, 0, step)

    def find_target_sum_ways(self, nums, start, S):
        if start == len(nums):
            return 1 if S == 0 else 0
        return self.find_target_sum_ways(nums, start+1, S+nums[start]) + \
            self.find_target_sum_ways(nums, start+1, S-nums[start])


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    # nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # S = 0
    # res = so.findTargetSumWays(nums, S)
    # print("res->", res)
    res = so.find_target_sum_ways(nums, 0, S)
    print("res->", res)
