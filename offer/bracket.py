from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """回溯法:将所有可能的组合打印出来-->挑选合格的"""
        # 二进制法构造括号组合0代表-->(,1代表-->)
        # 总共有2**3种
        ans = []
        n *= 2
        for i in range(2**(n - 1), 2**n):
            bin_n = bin(i)[2:]
            bracket = "".join(["(" if i == "1" else ")" for i in bin_n])
            if self.is_ok(bracket):
                ans.append(bracket)
        return ans

    def is_ok(self, input):
        """判断输入的括号是否合法"""
        stack = []
        if input.count("(") != input.count(")"):
            return False
        for ch in input:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
        return len(stack) == 0

    def get_ans(self, n):
        """构造解空间树求解答案"""
        ans = []
        self.dfs(ans, 1, 0, "(", n)
        return ans

    def dfs(self, ans, left, right, bracket, n):
        """深度递归构造解空间树"""
        if left + right == 2 * n:
            ans.append(bracket)
            return
        if left < n:
            self.dfs(ans, left + 1, right, bracket + "(", n)
        if right < n and right < left:
            self.dfs(ans, left, right + 1, bracket + ")", n)


if __name__ == "__main__":
    n = 3
    so = Solution()
    # res = so.generateParenthesis(n)
    # print(res)
    res = so.get_ans(n)
    print(res)
