import sys

class Solution:
    def helper(self,arr,n,i):
        if(n==0):
            return 0
        if(i<0):
            return sys.maxsize 
        if(n < arr[i]):
            return self.helper(arr,n,i-1)
            
        return min(self.helper(arr,n-arr[i],i)+1, self.helper(arr,n,i-1))
        
    def coinChange(self, coins, amount) -> int:
        return self.helper(coins,amount,len(coins)-1)
    
obj = Solution()
coins=[1,2,5]
a=11
print(obj.coinChange(coins,a))