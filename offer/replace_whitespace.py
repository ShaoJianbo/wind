

class Solution:
    def replaceSpace(self, s: str) -> str:
        """ 字符串s中的每个空格替换成"%20" """
        res = ""
        str_arr = s.split(" ")
        replace = "%20"
        res = f"{replace}".join(str_arr)
        return res


if __name__ == '__main__':
    so = Solution()
    s = '"We are happy."'
    res = so.replaceSpace(s)
    print(res)
