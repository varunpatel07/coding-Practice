import math
class Solution:
    def soln(self,cache,n):

        if(n==0):
            return False
        if(cache[n]!=None):
            return cache[n]
        i = 1
        while(i*i<=n):
            if(not self.soln(cache,n-i*i)):
                cache[n] =  True
                return cache[n]
            i+=1
        cache[n] =  False
        return cache[n]

    def winnerSquareGame(self, n: int) -> bool:
        #return self.soln([None]*(n+1),n)
        dp = [False]*(n+1)
        for i in range(1,n+1):
            for j in range(1,int(math.sqrt(i))+1):
                if(not dp[i-j*j]):
                    dp[i] = True
        return dp[n]
        

obj = Solution()
print(obj.winnerSquareGame(2))