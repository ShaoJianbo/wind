from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = float("INF")
        minutes = []
        for time in timePoints:
            hour, minute = time.split(":")
            minutes.append(int(hour) * 60 + int(minute))

        minutes.sort()
        print("time->", minutes)

        min_diff = min(min_diff, minutes[-1] - minutes[-2],
                       minutes[0] + 24 * 60 - minutes[-1])
        minutes.sort()
        for i in range(0, len(timePoints) - 1):
            min_diff = min(
                min_diff,
                minutes[i + 1] - minutes[i],
            )

        return min_diff


if __name__ == '__main__':
    so = Solution()
    timePoints = ["23:59", "00:00"]
    res = so.findMinDifference(timePoints)
    print(res)
