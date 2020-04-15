
class Solution:
    def countDigitOne(self, n: int) -> int:
        """找出1出现的次数"""
        ans = 0
        i = 0
        while i <= n:
            if i <= n and "1" in str(i):
                ans += str(i).count('1')
            i += 1
        return ans


if __name__ == '__main__':
    so = Solution()
    n = 12
    res = so.countDigitOne(n)
    print(res)
