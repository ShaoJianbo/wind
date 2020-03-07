class UnionFind(object):
    """并查集"""
    def __init__(self):
        self.parent = [i for i in range(0, 1002)]

    def find(self, n):
        """查找元素n的祖先节点"""
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, n1, n2):
        """将两个元素联通"""
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)
        if root_n1 == root_n2:
            return False
        self.parent[root_n2] = root_n1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        union_find = UnionFind()
        for edge in edges:
            start, end = edge
            if union_find.union(start, end) is False:
                return edge
        return []


if __name__ == '__main__':
    so = Solution()
    # edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

    edges = [[1, 2], [1, 3], [2, 3]]
    res = so.findRedundantConnection(edges)
    print(res)

    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res = so.findRedundantConnection(edges)
    print(res)
