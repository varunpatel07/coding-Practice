import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_stock = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            curr_stock = min(curr_stock,prices[i])
            max_profit  = max(max_profit,prices[i] - curr_stock)
        return max_profit
        