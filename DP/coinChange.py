import sys
class Solution:
    def __init__(self,a,l):
        self.cache = [[-1]*(a+1) for _ in range(l+1)]
    def coinChange(self, coins, amount,i) -> int:
        if(amount == 0):
            return 0
        if(i<0):
            return 1001
        if(self.cache[i][amount]!=-1):
            return self.cache[i][amount]
        if(coins[i-1]>amount):
            self.cache[i][amount] = self.coinChange(coins,amount,i-1)
        else:
            self.cache[i][amount] = min(self.coinChange(coins,amount - coins[i-1],i)+1, self.coinChange(coins,amount,i-1))
        return self.cache[i][amount]
    
    def coinChangeIter(self, coins, amount,i):
        for i in range(len(self.cache)):
            for j in range(len(self.cache[0])):
                if(j==0 and i==0):
                    self.cache[i][j] = 0
                elif(i==0):
                    self.cache[i][j] = 1001
                elif(j==0):
                    self.cache[i][j] = 0

        for i in range(1,len(self.cache)):
            for j in range(1,len(self.cache[0])):
                self.cache[i][j] = min(self.cache[i][j-1], self.cache[i-coins[i]][j]+1)
        print(self.cache[i][j])

        


coins = [2]
amount = 3 
obj = Solution(amount,len(coins))
for row in obj.cache:
    print(row)
print(obj.coinChange(coins,amount,len(coins)))
#print(obj.coinChangeIter(coins,amount,len(coins)))
for row in obj.cache:
    print(row)
