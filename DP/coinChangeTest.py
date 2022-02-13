import sys
class Solution:
    def __init__(self,row,col):
        self.cache = [[-1]*(col+1) for _ in range(row+1)]
    def coinChange(self, coins, amount,i=0) -> int:
        if(amount==0):
            self.cache[i][amount] = 0
            return 0
        if(self.cache[i][amount]!=-1):
            return self.cache[i][amount]
        if(i<0 or amount<0):
            return sys.maxsize
        self.cache[i][amount] = min(self.coinChange(coins,amount-coins[i],i)+1,self.coinChange(coins,amount,i-1))
        return self.cache[i][amount]

    def coinIterative(self,coins,amount):
        arr = [[-1] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            arr[i][0] = 0
        for i in range(1,amount+1):
            arr[0][i] = sys.maxsize
        for i in range(1,len(arr)):
            for j in range(1,len(arr[0])):
                if(j < coins[i-1]):
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = min(arr[i][j - coins[i-1]]+1,arr[i-1][j])

        for row in arr:
            print(row)
        return arr[len(coins)][amount]

obj = Solution(3,11)
arr =[4,2]
t = 4
#print(obj.coinChange(arr,t,len(arr)-1))
#for row in obj.cache:
#    print(row)
print(obj.coinIterative(arr,t))