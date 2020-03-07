class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        cnt = 0
        for i in range(len(s)):
            cnt += self.count_sub_str(s, i, i)
            cnt += self.count_sub_str(s, i, i + 1)
        return cnt

    def count_sub_str(self, s, start, end):
        cnt = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            cnt += 1
            start -= 1
            end += 1
        return cnt

    def get_dp(self, s):
        cnt = 0
        dp = [[1 if i == j else 0 for i in range(len(s))]
              for j in range(len(s))]
        i = len(s) - 1
        while i >= 0:
            j = i
            while j < len(s):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == 1):
                    cnt += 1
                    dp[i][j] = 1
                j += 1
            i -= 1
        return cnt


if __name__ == '__main__':
    so = Solution()
    s = "abc"
    s = "aaa"
    s = "aaaaa"
    res = so.countSubstrings(s)
    print(res)
    res = so.get_dp(s)
    print(res)
