from typing import List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    is_true = True

    def canFinish(self, class_num: int, pre_class: List[List[int]]) -> bool:
        ingress = [[0 for i in range(class_num)] for i in range(class_num)]
        one_cnt = 0

        for pair in pre_class:
            cur, pre = pair[0], pair[1]
            ingress[pre][cur] += 1
            one_cnt +=1

        queue = []
        # 将入度为0的节点放入队列
        for i in range(class_num):
            ingress_sum = sum([val[i] for val in ingress])  # 获取某一列元素
            j = 0
            if ingress_sum == 0:
                queue.append(i)

        i = class_num
        while len(queue)>0:
            class_order = queue.pop()

            for k in range(class_num):
                if ingress[class_order][k] > 0:
                    ingress[class_order][k] -= 1
                    one_cnt -=1
                # 获取列元素
                ingress_col = [val[k] for val in ingress]
                # 获取行元素
                ingress_row = ingress[k]
                if sum(ingress_col) == 0 and sum(ingress_row) > 0:
                    queue.append(k)

        if one_cnt == 0:
            return True
        return False

if __name__ == '__main__':
    so = Solution()
    num = 2
    pre = [[1, 0], [0, 1]]
    num = 2
    pre = [[1, 0]]
    # num = 3
    # pre = [[1, 0], [1, 2], [0, 1]]
    # num = 3
    # pre = [[1, 0], [2, 1]]
    res = so.canFinish(num, pre)
    print(res)
