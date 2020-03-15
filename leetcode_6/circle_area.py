class UnionFind(object):
    """并查集"""
    def __init__(self, num):
        self.parents = [i for i in range(num + 1)]

    def union(self, n1, n2):
        """连通->联通时要指向最大的父亲节点"""
        p1 = self.find(n1)
        p2 = self.find(n2)
        # 注意并查集的写法是self.parents[p2]-->p1
        if p1 != p2:
            self.parents[p2] = p1

    def find(self, n):
        """查找父节点"""
        while self.parents[n] != n:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def is_connected(self, n1, n2):
        """判断是否连通"""
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

        def node(x, y):
            """返回节点代表的数"""
            return x * col + y

        # 用一个虚拟节点,边界上的O的服节点都是这个虚拟节点
        uf = UnionFind(row * col + 1)
        dummy_node = row * col

        # 联通两类区域:边界上的O联通row+col, 内部的O联通相邻的O
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    if i in [0, row - 1] or j in [0, col - 1]:
                        uf.union(dummy_node, node(i, j))
                    else:
                        # 和上下左右合并成一个连通区域.
                        if i > 0 and board[i - 1][j] == 'O':
                            uf.union(node(i, j), node(i - 1, j))
                        if i < row - 1 and board[i + 1][j] == 'O':
                            uf.union(node(i, j), node(i + 1, j))
                        if j > 0 and board[i][j - 1] == 'O':
                            uf.union(node(i, j), node(i, j - 1))
                        if j < col - 1 and board[i][j + 1] == 'O':
                            uf.union(node(i, j), node(i, j + 1))

        print(uf.parents)
        for i in range(0, row):
            for j in range(0, col):
                if uf.is_connected(node(i, j), dummy_node):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        print(board)


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

    res = so.solve(board)
    print(res)
