class Solution:
    jumps = [0 for _ in range(101)]
    jumps[0] = 1
    jumps[1] = 1
    jumps[2] = 2

    def numWays(self, n: int) -> int:
        """青蛙跳台阶"""
        # 递推公司
        # jumps[n] = jumps[n-1]+jumsp[n-2]
        if n <= 2:
            return self.jumps[n]
        else:
            if self.jumps[n] > 0:
                return self.jumps[n]
            self.jumps[n] = self.numWays(n - 1) + self.numWays(n - 2)
            return self.jumps[n] % 1000000007


if __name__ == '__main__':
    so = Solution()
    n = 7
    res = so.numWays(n)
    print(res)
