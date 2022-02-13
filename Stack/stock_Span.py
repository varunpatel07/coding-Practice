"""
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than its price on the given day. 
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6} 

inp = [100, 80, 60, 70, 60, 75, 85]
op = [1, 1, 1, 2, 1, 4, 6]

intutuion -> variation of next greatest element in left
"""


class Solution:
    def stockSpan(self,inp):
        op = [0]*len(inp)
        s = []
        for i in range(len(inp)):
            while(s and s[-1][0]<=inp[i]):
                s.pop()
            op[i] = i-s[-1][1] if s else i+1
            s.append((inp[i],i))
        return op




        pass

obj = Solution()
print(obj.stockSpan([1,2,3,4,5]))