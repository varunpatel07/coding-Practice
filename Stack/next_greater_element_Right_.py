"""
given an array find the next largest element(to the Left of every element)
inp = [1,3,2,4]
op = [3,4,4,-1]
"""


class Solution:
    def nextGreatest(self,inp):
        op =[0] * len(inp)
        s = []
        for i in range(len(inp)-1,-1,-1):
            while(s and s[-1]<inp[i]):
                s.pop()
            if(s):
                op[i] = s[-1]
            else:
                op[i] = -1
            s.append(inp[i])
        return op



obj = Solution()
inp = [1,3,2,4]
print(obj.nextGreatest(inp))