class Solution:
    def translateNum(self, num: int) -> int:
        """将数字转换成字符串"""
        # 97-->a chr() int-->char
        # 有多少种翻译方法与数字的切分有关
        return self.backtrack(str(num), 0)

    def get_dp(self, n):
        str_n = str(n)
        dp = [1 for _ in range(len(str_n)+1)]
        for i in range(2, len(str_n)+1):
            print(f"{dp[i-2:i-1]}")
            dp[i] = dp[i-1]+dp[i-2] if 10 <= int(str_n[i-2:i]) <= 25 else dp[i-1]
        # print(dp)
        return dp[len(str_n)]

    def backtrack(self, str_n, pos):
        """得到字符串str_的拆分种类数"""
        size = len(str_n)
        print(f"pos->{pos}")
        if pos == size:
            return 1
        if str_n[pos] == '0' or pos == size-1 or str_n[pos:pos+2] > '25':
            return self.backtrack(str_n, pos + 1)
        else:
            return self.backtrack(str_n, pos+1) + self.backtrack(str_n, pos+2)


if __name__ == '__main__':
    so = Solution()
    num = 12258
    # res = so.translateNum(num)
    # print(res)
    res = so.get_dp(num)
    print(res)