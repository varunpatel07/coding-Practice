"""
find next greater element to the left
i/p = [1,3,2,4]
o/p = [-1,-1,3,-1]
"""

class Solution:
    def nextGreaterElement(self,inp):
        op = [0] * len(inp)
        s = []
        for i in range(len(inp)):
            while(s and s[-1]< inp[i]):
                s.pop()
            op[i] = s[-1] if s else -1
            s.append(inp[i])
        return op




obj = Solution()
inp = [1,3,2,4]
print(obj.nextGreaterElement(inp))