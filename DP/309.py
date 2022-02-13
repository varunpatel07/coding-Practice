"""
Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
    Input: prices = [1]
    Output: 0
"""

from functools import lru_cache
class Solution:
    def maxProfit(self, prices) -> int:
        @lru_cache(None)
        def dp(i,h):
            if(i>=len(prices)):
                return 0 
            n = dp(i+1,h)
            s = 0
            if(h):
                s = dp(i+2,0) + prices[i]
            else:
                s = dp(i+1,1) + (-1*prices[i])
            return max(s,n)
        return dp(0,0)


    def maxProfitDp(self,prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]
        for i in range(len(prices)-1,-1,-1):
            for h in range(2):
                n = dp[i+1][h]
                s = 0
                if(h):
                    s = dp[i+2][0] + prices[i]
                else:
                    s = dp[i+1][1] + (-1*prices[i])
                dp[i][h] = max(s,n)
        return dp[0][0]
        pass

obj = Solution()
arr = [1,2,3,0,2]
print(obj.maxProfitDp(arr))
