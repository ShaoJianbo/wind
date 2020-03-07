from typing import List


class Solution(object):
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):  # 从每个点开始
            s = set()  # 集合记录走过的点
            pos = start  # 当前位置
            pos_last = pos  # 上次的位置
            flag = 0  # 标志位
            print("A->start:{0}, set:{1}, pos_last:{2}, flag->{3}".format(pos, s, pos_last, flag))
            while pos not in s:  # 未出现环，便继续循环
                flag = 1
                s.add(pos)
                pos_last = pos
                pos = (pos + nums[pos] + n) % n  # 新的位置
                if nums[pos] * nums[start] < 0:  # 出现反向，则无效
                    flag = 2
                    break
            print("B->start:{0}, set:{1}, pos_last:{2}, flag->{3}".format(pos, s, pos_last, flag))
            if pos == pos_last:  # 循环长度为1时，路径无效
                continue
            if len(s) > 1 and flag == 1:  # 循环长度>1, 且出现环
                return True

        return False


if __name__ == '__main__':
    so = Solution()
    nums = [2, -1, 1, 2, 2]

    res = so.circularArrayLoop(nums)
    print(res)
