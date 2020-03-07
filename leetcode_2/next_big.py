from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        last_num = nums2[-1]
        i = len(nums2) - 2
        wait = [0 for n in nums2]  # 保存比自己大元素的索引
        next_arr = {last_num: -1}
        while i >= 0:
            cur_num = nums2[i]
            if cur_num < last_num:
                wait[i] = 1
            else:
                next_step = i + 1
                last_num = nums2[next_step]
                while cur_num >= last_num and wait[
                        next_step] > 0 and next_step < len(nums2) - 1:
                    next_step += wait[next_step]
                    last_num = nums2[next_step]
                if cur_num < last_num:
                    wait[i] = next_step - i
            if wait[i] > 0:
                next_arr[nums2[i]] = nums2[i + wait[i]]
            else:
                next_arr[nums2[i]] = -1
            last_num = nums2[i]
            i -= 1

        res = [0 for i in nums1]
        for i, n in enumerate(nums1):
            res[i] = next_arr.get(n, -1)
        return res


if __name__ == '__main__':
    so = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    # nums1 = [2, 4]
    # nums2 = [1, 2, 3, 4]
    # nums1 = [2, 1, 3]
    # nums2 = [2, 3, 1]
    # nums1 = [1, 3, 5, 2, 4]
    # nums2 = [6, 5, 4, 3, 2, 1, 7]
    res = so.nextGreaterElement(nums1, nums2)
    print(res)
