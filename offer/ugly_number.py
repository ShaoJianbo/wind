class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        idx2 = idx3 = idx5 = 0
        while len(ans) < n:
            a = ans[idx2] * 2
            b = ans[idx3] * 3
            c = ans[idx5] * 5
            min_n = min(a, b, c)
            if min_n not in ans:
                ans.append(min_n)
            if min_n == a:
                idx2 += 1
            elif min_n == b:
                idx3 += 1
            else:
                idx5 += 1
        print(ans)
        return ans[n-1]


if __name__ == '__main__':
    so = Solution()
    n = 10
    res = so.nthUglyNumber(n)
    print(res)