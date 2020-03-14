class UnionFind:
    def __init__(self, num):
        self.parents = [i for i in range(num + 1)]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 != p2:
            self.parents[n2] = p1

    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def is_connected(self, n1, n2):
        return self.find(n1) == self.find(n2)


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) < 1 or len(board[0]) < 1:
            return
        row = len(board)
        col = len(board[0])

        def node_num(x, y):
            """返回节点代表的数"""
            return x * col + y

        uf = UnionFind(row * col + 1)
        dummy_node = row * col

        # 联通两类区域:边界上的O联通row+col, 内部的O联通相邻的O
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    if i in [0, row - 1] or j in [0, col - 1]:
                        uf.union(dummy_node, node_num(i, j))
                        if i > 0 and board[i - 1][j] == "O":
                            uf.union(dummy_node, node_num(i - 1, j))
                        # 连通下节点
                        if i < row - 1 and board[i + 1][j] == "O":
                            uf.union(dummy_node, node_num(i + 1, j))
                        # 连通左节点
                        if j > 0 and board[i][j - 1] == "O":
                            uf.union(dummy_node, node_num(i, j - 1))
                        # 连通右节点
                        if j < col - 1 and board[i][j + 1] == "O":
                            uf.union(dummy_node, node_num(i, j + 1))
                    else:
                        self.set_next_node(board, col, i, j, node_num, row, uf, dummy_node)

        print(uf.parents)
        for i in range(0, row):
            for j in range(0, col):
                if uf.is_connected(node_num(i, j), dummy_node):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        print(board)

    @staticmethod
    def set_next_node(board, col, i, j, node_num, row, uf, dummy_node):
        """设置邻居节点的值"""
        flag = uf.is_connected(node_num(i,j), dummy_node)

        if i > 0 and board[i - 1][j] == "O":
            if flag:
                uf.union(dummy_node, node_num(i-1, j))
            else:
                uf.union(node_num(i, j), node_num(i - 1, j))
        # 连通下节点
        if i < row - 1 and board[i + 1][j] == "O":
            if flag:
                uf.union(dummy_node, node_num(i+1, j))
            else:
                uf.union(node_num(i, j), node_num(i + 1, j))
        # 连通左节点
        if j > 0 and board[i][j - 1] == "O":
            if flag:
                uf.union(dummy_node, node_num(i,j-1))
            else:
                uf.union(node_num(i, j), node_num(i, j - 1))
        # 连通右节点
        if j < col - 1 and board[i][j + 1] == "O":
            if flag:
                uf.union(dummy_node, node_num(i, j+1))
            else:
                uf.union(node_num(i, j), node_num(i, j + 1))


if __name__ == '__main__':
    so = Solution()
    board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]

    board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]

    board = [["O", "X", "O", "O", "O", "O", "O", "O", "O"],
             ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
             ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
             ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
             ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
             ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
             ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
             ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
             ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]

    my = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    ans = [["O", "X", "O", "O", "O", "O", "O", "O", "O"],
           ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
           ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
           ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
           ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
           ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
           ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
           ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
           ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]
    res = so.solve(board)

    print(res)
