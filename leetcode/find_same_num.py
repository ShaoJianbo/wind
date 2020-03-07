class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print("slow {0}--> fast {1}".format(slow, fast))
            if slow == fast:
                break

        print(slow)
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2, 5]
    so = Solution()
    res = so.findDuplicate(nums)
    print(res)
