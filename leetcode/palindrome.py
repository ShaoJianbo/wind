class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        i = 0
        while i < len(s):
            count += self.count_string_palindrome(s, i, i)
            count += self.count_string_palindrome(s, i, i + 1)
            i += 1
        return count

    @staticmethod
    def count_string_palindrome(string, left, right):
        count = 0
        current = (right < len(string) and string[left] == string[right])
        while current and \
                left >= 0 and \
                right < len(string) and \
                string[left] == string[right]:
            count += 1
            left -= 1
            right += 1
        return count


if __name__ == "__main__":
    so = Solution()
    s = ""
    res = so.countSubstrings(s)
    print(res)
