class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.get_num(nums, k)

    def get_num(self, nums, k):
        hash = {0: 1}
        sum_nums = 0
        count = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            if sum_nums - k in hash:
                count += hash[sum_nums - k]
            if sum_nums in hash:
                hash[sum_nums] += 1
            else:
                hash[sum_nums] = 1
        return count


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    nums = [100, 1, 2, 3, 4]
    k = 3
    print("nums-->", nums, "k-->", k)
    so = Solution()
    res = so.subarraySum(nums, k)
    print(res)
