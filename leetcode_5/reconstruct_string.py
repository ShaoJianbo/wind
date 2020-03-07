class Solution:
    def reorganizeString(self, S: str) -> str:
        work_map = [[0, chr(ord('a') + i)] for i in range(26)]
        for s in S:
            work_map[ord(s) - ord('a')][0] += 1
        work_map.sort()
        print("B->", work_map)
        new_str = ""
        while work_map[-1][0] > 0:
            j = 0
            # 数量最多的字符和第二多的字符轮流填写
            while j < 2 and work_map[25 - j][0] > 0:
                # print("new_str->",new_str, "add_str->", work_map[25-j][1])
                if len(new_str) > 0 and work_map[25 - j][1] == new_str[-1]:
                    return ""
                new_str += work_map[25 - j][1]
                work_map[25 - j][0] -= 1
                j += 1
            work_map.sort()

        return new_str


if __name__ == '__main__':
    so = Solution()
    S = "aab"
    S = "aaab"
    S = "vvvlo"
    res = so.reorganizeString(S)
    print(res)
