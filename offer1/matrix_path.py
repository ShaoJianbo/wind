from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        def dfs(i, j, k):
            if not 0 <= i < len(board) or \
                    not 0 <= j < len(board[0]) or \
                    board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            # 这样写法有助于快速返回-->减少执行时间
            ans = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(
                i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = tmp
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                res = dfs(i, j, 0)
                if res:
                    return True
        return False


if __name__ == '__main__':
    so = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    res = so.exist(board, word)
    print(res)
