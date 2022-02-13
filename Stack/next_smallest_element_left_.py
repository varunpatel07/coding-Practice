"""
given an array find the next smaller element(to the right of every element)
inp = [4,5,2,10,8]
op = [-1,4,-1,2,2]
"""


class Solution:
    def nextSmallest(self,inp):
        op =[0] * len(inp)
        s = []
        for i in range(len(inp)):
            while(s and s[-1]>inp[i]):
                s.pop()
            op[i] = s[-1] if s else -1
            s.append(inp[i])
        return op
    




obj = Solution()
inp = [4,5,2,10,8]
print(obj.nextSmallest(inp))