class Solution(object):
    def find_same_num(self, arr, num):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= num:
                right = mid
            else:
                left = mid + 1

        if arr[right] == num:
            return right
        else:
            return -1


if __name__ == "__main__":
    so = Solution()
    arr = [2, 3, 3, 4, 5, 5, 5, 6, 7]
    num = 5
    index = so.find_same_num(arr, num)
    print(f"index-->{index}")
