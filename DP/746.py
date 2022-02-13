
from cmath import cos
import sys
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        #return self.minCostClimbingStairsdp(cost)
        cache = {}
        def climbstairs(cost,i):
            if(i<0):
                return 0
            #if(i==0 or i==1):
            #    return cost[i]
            if i not in cache:
                cache[i] =  min(climbstairs(cost,i-1),climbstairs(cost,i-2))+cost[i]
            return cache[i]
    
        return min(climbstairs(cost,len(cost)-1),climbstairs(cost,len(cost)-2))

    def minCostClimbingStairsdp(self,cost):
        dp = [-1]*len(cost)
        dp[0] = cost[0] #cost for reaching from stair 0 is same as cost because we need to take 1 step
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[len(cost)-1],dp[len(cost)-2])



obj = Solution()
cost = [10,15,20]
print(obj.minCostClimbingStairs(cost))