class Solution:
    fib_arr = [0 for _ in range(101)]
    fib_arr[1] = 1

    def fib(self, n: int) -> int:
        """
        :param n:
        :return:
        """
        fib_arr = [0 for _ in range(101)]
        fib_arr[1] = 1

        def help(n):
            pass
        if n <= 1:
            return self.fib_arr[n]
        if self.fib_arr[n] != 0:
            return self.fib_arr[n]
        else:
            self.fib_arr[n] = self.fib(n-1) + self.fib(n-2)
            # return self.fib_arr[n]
            return self.fib_arr[n] % 1000000007


if __name__ == '__main__':
    so = Solution()
    n = 2
    res = so.fib(45)
    print(so.fib_arr)
    print(res)