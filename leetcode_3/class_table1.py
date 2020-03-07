from typing import List


class Solution:
    def canFinish(self, class_num: int,
                  class_relations: List[List[int]]) -> bool:
        if not class_relations or class_num == 1:
            return True
        # 保存每个节点的入度
        ingress = [0 for _ in range(class_num)]
        # 保存每个节点的邻接关系
        adjacent_edges = [[] for _ in range(class_num)]
        for [cur, pre] in class_relations:
            ingress[cur] += 1
            adjacent_edges[pre].append(cur)
        print(adjacent_edges)
        # 广度优先遍历
        queue = []
        for edge, num in enumerate(ingress):
            if num == 0:
                queue.append(edge)
        while queue and class_num:
            pre = queue.pop()
            class_num -= 1
            for cur in adjacent_edges[pre]:
                ingress[cur] -= 1
                if not ingress[cur]:
                    queue.append(cur)
        return sum(ingress) == 0

    def canFinish(self, class_num: int,
                  class_relations: List[List[int]]) -> bool:

        adjacent_edges = [[] for _ in range(class_num)]
        for cur, pre in class_relations:
            adjacent_edges[pre].append(cur)

        def dfs(i, adjacent_edges, flags):
            if flags[i] == 1:
                return False
            if flags[i] == -1:
                return True
            flags[i] = 1
            for adj in adjacent_edges[i]:
                res = dfs(adj, adjacent_edges, flags)
                if not res:
                    return False
            flags[i] = -1
            return True

        # 0->没有访问 1->已经访问 -1->其他节点访问
        # 深度优先遍历
        flags = [0 for _ in range(class_num)]
        for edge in range(class_num):
            res = dfs(edge, adjacent_edges, flags)
            if not res:
                return False

        return True


if __name__ == '__main__':
    so = Solution()
    num = 2
    pre = [[1, 0], [0, 1]]
    # num = 2
    # pre = [[1, 0]]
    num = 3
    pre = [[0, 1], [0, 2], [1, 2]]
    # num = 3
    # pre = [[1, 0]]
    res = so.canFinish(num, pre)
    print(res)
