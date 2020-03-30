class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) ==0:
            return 0
        low = 0
        result = 1
        for high in range(1, len(s)):
            if s[high] not in s[low:high]:
                result = max(result, high-low+1)
                # print(s[low:high], s[high], result)
            else:
                while s[high] in s[low:high]:
                    low += 1
                # result = max(result, high - low + 1)
        return result


if __name__ == "__main__":
    so = Solution()
    s = "abcabcbb"
    s = "bbbb"
    # s = "aab"
    # s = "dvdf"
    s = "pwwkew"
    s = "au"
    res = so.lengthOfLongestSubstring(s)
    print(res)
