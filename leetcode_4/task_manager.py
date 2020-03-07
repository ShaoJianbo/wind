from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = [0 for _ in range(26)]
        for task in tasks:
            task_map[ord(task) - ord("A")] += 1

        print("task_map->", task_map)
        # 对数组进行逆序排序,执行次数越多的任务越靠后
        task_map.sort()
        print("task_map->", task_map)
        time = 0
        while task_map[25]:
            i = 0
            # n+1个任务为一轮,每次选择执行此处最多的任务执行
            while i <= n:
                # 如果没有任务执行则退出
                if task_map[25] == 0:
                    break
                # 如果任务的种类t少于n+1个,就只选择全部的t种任务
                if i < 26 and task_map[25 - i] > 0:
                    task_map[25 - i] -= 1

                # 没任务执行也要占用空闲时间
                time += 1
                i += 1
            task_map.sort()
        return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B", "D"]
    n = 2
    so = Solution()
    res = so.leastInterval(tasks, n)
    print(res)
