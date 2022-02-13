"""
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
"""
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        def dp(i,t,h):
            if(i>=len(prices) or t==0):
                return 0
            n = dp(i+1,t,h)
            s = 0
            if(h):
                s = dp(i+1,t-1,0)+prices[i]
            else:
                s = dp(i+1,t,1)+ (-1*prices[i])
            return max(n,s)

        return dp(0,k,0)

    def maxProfitdp(self,k,prices):
        n = len(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for t in range(1,k+1):
                for h in range(2):
                    n = dp[i+1][t][h]
                    s = 0
                    if(h):
                        s = dp[i+1][t-1][0]  + prices[i]
                    else:
                        s = dp[i+1][t][1] + (-1*prices[i])
                    dp[i][t][h] = max(n,s)
        return dp[0][k][0]

        
        pass


obj = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(obj.maxProfitdp(k,prices))