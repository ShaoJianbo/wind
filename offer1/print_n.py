from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_num = 0
        for i in range(1, n + 1):
            max_num = 10 * (max_num) + 9
        print(max_num)

        return [i for i in range(1, max_num + 1)]


if __name__ == '__main__':
    so = Solution()
    n = 1
    res = so.printNumbers(n)
    print(res)
