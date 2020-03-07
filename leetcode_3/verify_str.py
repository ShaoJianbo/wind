# 验证回文串


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        pre = 0
        last = len(s) - 1
        while pre <= last:
            print(pre, "->", last)
            while pre<=last and not s[pre].isalnum():
                pre += 1
            while pre<=last and not s[last].isalnum():
                last -= 1
            if pre<=last and s[pre].lower() != s[last].lower():
                print("pre->last", pre, "->", last, s[pre], s[last])
                return False
            while pre<=last and s[pre].lower() == s[last].lower():
                print(pre, last)
                pre += 1
                last -= 1

        print(pre, last)
        return True


if __name__ == '__main__':
    so = Solution()
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = ""
    s = "a."
    s = ".,"
    res = so.isPalindrome(s)
    print(res)
