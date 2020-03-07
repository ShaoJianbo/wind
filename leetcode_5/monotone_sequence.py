from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = [0 for i in range(len(A))]
        num = len(A)
        i = 0
        cur = A[0]
        while i < num:

            if cur < A[i]:
                flag[i] = 1
            elif cur > A[i]:
                flag[i] = -1
            cur=A[i]
            i += 1

        print(flag)
        if 1 in flag and -1 in flag:
            return False
        return True


if __name__ == '__main__':
    so = Solution()
    A = [1, 2, 2, 3]
    A = [6, 5, 4, 4]
    A = [1, 3 ,2]
    res = so.isMonotonic(A)
    print(res)
