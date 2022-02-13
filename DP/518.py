"""
Input: amount = 5, coins = [1,2,5]
Output: 4
"""


from functools import lru_cache


class Solution:
    @lru_cache(None)
    def dp(self,coin,a,i):
        if(a==0):
            return 1
        if(i>=len(coin) or a<0):
            return 0
        if(coin[i]>a):
            return self.dp(coin,a,i+1)

        return self.dp(coin,a,i+1) + self.dp(coin,a - coin[i],i)

    def change(self, amount: int, coins) -> int:
        return self.dp(coins,amount,0)

    def changedp(self,amount,coins):
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        for i in range(len(coins)+1):
            dp[i][0] = 1

        for i in range(len(coins)-1,-1,-1):
            for a in range(1,amount+1):
                if(coins[i] > a):
                    dp[i][a] = dp[i+1][a]
                else:
                    dp[i][a] = dp[i+1][a] + dp[i][a-coins[i]]
        for _ in dp:
            print(_)
        return dp[0][amount]

    
        pass

obj = Solution()
a = 5
c = [1,2,5]

print(obj.changedp(a,c))
"""  
     0 1 2 3 4 5

0    1 1 2 2 3 4 
1    1 0 1 0 1 1
2    1 0 0 0 0 1
3    1 0 0 0 0 0
"""