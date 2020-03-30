
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = num //2+1
        i = 0
        while i*i <= num and i<=a:
            if i*i == num:
                return True
            i+=1
        return False


if __name__ == "__main__":
    so = Solution()
    n = 9
    res = so.isPerfectSquare(n)
    print(res)