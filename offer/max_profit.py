from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """卖股票的最大利润"""
        # 在数组中找到两个数，使这两个数的差值最大，要求后面的数减去前面的
        max_profit = 0
        if not prices:
            return max_profit
        min_price = prices[0]
        for i in range(1, len(prices)):

            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

            # print(min_price,"->", max_profit)
        return max_profit


if __name__ == '__main__':
    so = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]
    res = so.maxProfit(prices)
    print(res)
