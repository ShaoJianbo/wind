# 并查集寻找陆地的连通域个数
from typing import List


class UnionFind(object):
    def __init__(self, num):
        self.parents = [i for i in range(num + 1)]

    def find(self, n):
        while self.parents[n] != n:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 < p2:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1

    def is_connected(self, n1, n2):
        return self.find(n1) == self.find(n2)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 思路将陆地和岛屿各自形成连通域，最后计算陆地的联通域个数
        if not grid or len(grid) < 1 or len(grid[0]) < 1:
            return 0
        row = len(grid)
        col = len(grid[0])

        def node(x, y):
            return x * col + y

        uf = UnionFind(row * col + 1)
        dummy_node = row * col + 1
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "1":
                    # uf.union(node(i, j), dummy_node)
                    if i > 0 and grid[i - 1][j] == "1":
                        uf.union(node(i, j), node(i - 1, j))
                    if i < row - 1 and grid[i + 1][j] == "1":
                        uf.union(node(i, j), node(i + 1, j))

                    if j > 0 and grid[i][j - 1] == "1":
                        uf.union(node(i, j), node(i, j - 1))

                    if j < col - 1 and grid[i][j + 1] == "1":
                        uf.union(node(i, j), node(i, j + 1))

        # print(uf.parents)
        start = 0
        for i in range(row):
            print(uf.parents[start:start + col])
            start += col

        island_num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and uf.find(node(i, j)) == node(i, j):
                    island_num += 1
        return island_num


if __name__ == "__main__":
    so = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    res = so.numIslands(grid)
    print(res)
