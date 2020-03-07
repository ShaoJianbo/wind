from typing import List


class Solution:
    def findOrder(self, num_courses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # 广度优先遍历
        ingress = [0 for _ in range(num_courses)]
        # adjacent
        adjacent = [[] for _ in range(num_courses)]
        for [cur, pre] in prerequisites:
            ingress[cur] += 1
            adjacent[pre].append(cur)

        queue = []
        for i in range(num_courses):
            if ingress[i] == 0:
                queue.append(i)

        # 保存上课顺序
        order = []
        while queue:

            pre = queue.pop()
            order.append(pre)

            loop_arr = list(adjacent[pre])
            for cur in loop_arr:
                ingress[cur] -= 1
                adjacent[pre].remove(cur)

            for cur in range(num_courses):
                if ingress[cur] == 0 and adjacent[cur] and cur not in queue:
                    queue.append(cur)

        class_ok = sum(ingress) == 0
        if not class_ok:
            return []
        print(order)
        for cur in range(num_courses):
            if cur not in order:
                order.append(cur)
        return order


if __name__ == '__main__':
    numCourse = 3
    # pres = [[1, 0], [2, 0]]
    pres = [[0, 1], [0, 2], [1, 2]]
    # pres = [[1,0]]
    so = Solution()
    res = so.findOrder(numCourse, pres)
    print("res->", res)
