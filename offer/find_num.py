from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """利用异或算法并将a和b分离出来"""
        # 1.两个独特的数字分成不同组
        # 2.相同的数字分成同组
        # 异或满足交换律 17xor19xor17=>17xor17xor19=19
        ans = 0
        a = 0
        b = 0
        for n in nums:
            ans ^= n
        print(f"a XOR b => {ans}")

        h = 1
        # 由于异或的性质是:同一位相同则为0,不同则为1
        # 将所有数字异或的结果一定不是0,至少有一位是1
        # 找到有差异的比特数-->重新遍历数组
        while ans & h == 0:
            print(f"h=>{h}")
            h <<= 1
        print(f"h-->{h}")

        # 重新遍历数组-->和差异比特数异或
        # 得到0后-->找到n-->与
        for n in nums:
            if h & n == 0:
                print(f"n1==>{n}")
                a ^= n
            else:
                print(f"n2==>{n}")
                b ^= n

        return [a, b]


if __name__ == '__main__':
    so = Solution()
    nums = [4, 1, 4, 6]
    res = so.singleNumbers(nums)
    print(res)
