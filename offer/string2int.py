import re


class Solution:
    # ^匹配开头
    # [\+\-]匹配一个+号或一个-号
    # ？前面的字符可有可无
    # \d 一个数字
    # + 前面的字符一个或多个
    def strToInt(self, str_num) -> int:
        expr = re.findall('^[\+\-]?\d+', str_num.lstrip())
        num = int(*expr)
        num = int(num)
        if num > (1 << 31) - 1:
            return (1 << 31) - 1
        if num < -(1 << 31):
            return -(1 << 31)
        return num


if __name__ == '__main__':
    so = Solution()
    str = "   -42"
    # str = "4193 with words"
    # str = "-91283472332"
    # str = "3.14159"
    # str = "-"
    # str = "+1"
    # str = " "
    # str = "-+1"
    # str = "42"
    # str = "2147483646"
    res = so.strToInt(str)
    print(res)
