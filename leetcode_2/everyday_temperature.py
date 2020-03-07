from typing import List


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        wait = [0 for n in range(len(t))]
        last_num = t[-1]
        i = len(t) - 2
        while i >= 0:
            cur_num = t[i]
            if cur_num < last_num:
                wait[i] = 1
            else:
                next_index = i + 1
                last_num = t[next_index]
                while cur_num >= last_num and \
                      next_index < len(t) - 1 and \
                      wait[next_index] > 0:
                    next_index += wait[next_index]
                    last_num = t[next_index]
                if cur_num < last_num:
                    wait[i] = next_index - i
            last_num = t[i]
            i -= 1

        return wait


if __name__ == '__main__':
    so = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [34, 80, 80, 34, 34, 80, 80, 80, 80, 34]
    temperatures = [34, 34, 47, 47, 34, 34, 34, 47, 34, 47, 47, 47, 34, 34, 34,
                    47, 34, 34, 47, 34, 47, 34, 34, 34, 34]
    res = so.dailyTemperatures(temperatures)
    print(res)
