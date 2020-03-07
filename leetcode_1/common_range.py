class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []
        if not B:
            return []
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            # print("A->", A, "i->", i)
            # print("B->", B, "j->", j)
            if start <= end:
                # print("start->", start, "end->", end)
                res.append([start, end])
                if end >= A[i][1]:
                    i += 1
                elif end >= B[j][1]:
                    j += 1
            elif A[i][0] >= B[j][1]:
                j += 1
            elif B[j][0] >= A[i][0]:
                i += 1
        return res


if __name__ == '__main__':
    so = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    # A = [[0, 4], [7, 8], [12, 19]]
    # B = [[0, 10], [14, 15], [18, 20]]
    # res = [[0, 4], [7, 8], [14, 15], [18, 19]]
    print("res-->", res)
    res = so.intervalIntersection(A, B)
    print("res-->", res)
