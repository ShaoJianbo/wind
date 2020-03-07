# -*- coding:utf8 -*-


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(str_res="", left=0, right=0):
            """回溯算法"""
            if len(str_res) == 2 * n:
                ans.append(str_res)
                return
            if left < n:
                backtrack(str_res + "(", left + 1, right)
            if right < left:
                backtrack(str_res + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans


if __name__ == "__main__":
    so = Solution()
    # n = 3
    # res = so.generateParenthesis(n)
    # print(res)
    n = 11
    res = so.generateParenthesis(n)
    print(res)
