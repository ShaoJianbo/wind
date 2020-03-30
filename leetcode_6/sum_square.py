import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """判断是否存在某个数是两个数的平方之和"""
        if c < 0:
            return False
        a = 0
        b = int(math.sqrt(c))
        while a <= b:
            print(f"{a}-->{b}")
            if a**2 + b**2 == c:
                return True
            elif a**2 + b**2 < c:
                a += 1
            else:
                b -= 1
        return a**2 + b**2 == c or c == 0

    def judge(self, c):
        for i in range(0, c+1):
            if i*i > c:
                return False
            b = c - i*i
            # print(f"i->{i} b->{b}")
            if self.binary_search(0, i, b):
                return True
        return False

    def binary_search(self, start, end, n):
        # print(f"[{start}-->{end}]:{n}")
        if start > end:
            return False
        mid = start + (end - start) // 2
        # print(f"mid->{mid}")
        if mid*mid == n:
            return True
        elif mid*mid < n:
            return self.binary_search(mid+1, end, n)
        else:
            return self.binary_search(start, mid - 1, n)


if __name__ == "__main__":
    so = Solution()
    n = 8
    n = 1
    n = 9
    res = so.judge(n)
    print(res)
