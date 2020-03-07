from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [x for x in range(n-1)]
        if not res or sum(res) != 0:
            res.append(-sum(res))
        return res


if __name__ == '__main__':
    so = Solution()
    n = 1
    res = so.sumZero(n)
    print(res)
