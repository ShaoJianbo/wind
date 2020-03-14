from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """回溯算法"""
        self.word = word
        row = len(board)
        col = len(board[0])
        for i in range(0, row):
            for j in range(0, col):
                visited = set()
                is_exist = self.find_words(board, i, j, "", visited)
                if is_exist:
                    return True
        return False

    def find_words(self, board, row, col, str_, visited):
        """采用回溯算法查找字符word"""
        # 判断字符串是否在word中
        if str_ not in self.word:
            return False
        # 判断字符串的首字母是否和查找单词一样
        if len(str_) > 0 and str_[0] != self.word[0]:
            return False
        # 判断字符串的长度是否满足要求
        # 判断字符串是否有重复字母被访问
        if len(str_) > len(self.word) or (row, col) in visited:
            return False
        str_ += board[row][col]
        if self.word == str_:
            return True
        # i,j-->(i,j+1) (i-1,j) (i,j-1) (i+1,j)
        # 向右走
        cur_pos = (row, col)
        if 0 <= row < len(board) and 0 <= col + 1 < len(board[0]):
            visited.add(cur_pos)
            right = self.find_words(board, row, col + 1, str_, visited)
            visited.remove(cur_pos)
            if right:
                return True
        # 向左走
        if 0 <= row < len(board) and 0 <= col - 1 < len(board[0]):
            visited.add(cur_pos)
            left = self.find_words(board, row, col - 1, str_, visited)
            visited.remove(cur_pos)
            if left:
                return True
        # 向下走
        if 0 <= row + 1 < len(board) and 0 <= col < len(board[0]):
            visited.add(cur_pos)
            down = self.find_words(board, row + 1, col, str_, visited)
            visited.remove(cur_pos)
            if down:
                return down
        # 向上走
        if 0 <= row - 1 < len(board) and 0 <= col < len(board[0]):
            visited.add(cur_pos)
            top = self.find_words(board, row - 1, col, str_, visited)
            visited.remove(cur_pos)
            if top:
                return top


if __name__ == '__main__':
    so = Solution()
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "SEE"
    board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"],
             ["a", "b", "a", "a", "a", "b"], ["a", "b", "a", "b", "b", "a"],
             ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
             ["a", "a", "b", "a", "a", "b"]]
    word = "aabbbbabbaababaaaabababbaaba"
    res = so.exist(board, word)
    print(res)
