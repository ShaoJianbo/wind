from functools import reduce

class Solution:
    def sumNums(self, n: int) -> int:
        def add(x,y):
            return x+y
        arr = [i for i in range(1, n+1)]
        return reduce(add, arr)

        # return n and n + self.sumNums(n-1)



if __name__ == '__main__':
    so = Solution()
    for i in [1,2,3]:
        res = so.sumNums(i)
        print(res)