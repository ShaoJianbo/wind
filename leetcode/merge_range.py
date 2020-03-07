class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals
        # 对每个小区间进行合并排序
        intervals.sort(key=lambda x: x[0])
        # print("interval-->", intervals)
        i = 0
        res = []
        while i <= len(intervals) - 1:
            # print("cur-->", intervals[i])
            cur_left = intervals[i][0]
            cur_right = intervals[i][1]
            j = i + 1
            while j <= len(intervals) - 1 and intervals[j][0] <= cur_right:
                cur_right = max(cur_right, intervals[j][1])
                j += 1
            if len(res) > 0 and cur_left <= res[-1][1]:
                pass
            else:
                res.append([cur_left, cur_right])
            i += 1
        return res

    def merge_ok(self, intervals):
        if not intervals:
            return intervals
        # 对每个小区间进行合并排序
        intervals.sort(key=lambda x: x[0])
        print("interval-->", intervals)
        i = 0
        res = []
        while i <= len(intervals) - 1:
            print("cur-->", intervals[i])
            if len(res)<1 or intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            i += 1
        return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
    so = Solution()
    res = so.merge_ok(intervals)
    print(res)
