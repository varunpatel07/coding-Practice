class Solution:
    def minCost(self, s, cost) -> int:
        if(len(s)==1):
            return 0
        min_cost,j=0,0
        i=1
        while(i<len(s)):
            if(s[i]==s[j]):
                if(cost[i]<cost[j]):
                    min_cost+=cost[i]
                else:
                    min_cost+=cost[j]
                    j = i
            else:
                j=i

            i+=1
        return min_cost

s= "cddcdcae"
cost = [4,8,8,4,4,5,4,2]
obj = Solution()
print(obj.minCost(s,cost))