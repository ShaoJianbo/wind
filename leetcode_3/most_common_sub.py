class Solution:
    def longestCommonSubsequence(self, txt1: str, txt2: str) -> int:
        short, long = [
            len(txt1), len(txt2)
        ] if len(txt1) < len(txt2) else [len(txt2), len(txt1)]

        if len(txt1) > len(txt2):
            txt1, txt2 = txt2, txt1
        dp = [["" for _ in range(long + 1)] for _ in range(short + 1)]
        # print("dp->", dp, "text1->", text1, "text2->", text2)
        # dp[i][j] == dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1] + text1[i]
        max_len = 0
        for i in range(0, short):
            j = 0
            while j < long:
                if i == 0 and j >= 0:
                    if txt1[i] == txt2[j]:
                        dp[i][j] = txt1[i]
                        max_len = max(max_len, len(dp[i][j]))
                        print("A:{0}->{1}".format(i, j), "dp[i][j]", dp[i][j])
                if txt1[i] == txt2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + txt2[j]
                    max_len = max(max_len, len(dp[i][j]))
                    print("B:{0}->{1}".format(i, j), "dp[i][j]", dp[i][j])
                else:
                    if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
                    max_len = max(max_len, len(dp[i][j]))
                    print("C:{0}->{1}".format(i, j), "dp[i][j]", dp[i][j])
                j += 1
        # print(dp)

        return max_len


if __name__ == '__main__':
    so = Solution()
    text1 = "abcde"
    text2 = "ace"
    res = so.longestCommonSubsequence(text1, text2)
    print(res)
