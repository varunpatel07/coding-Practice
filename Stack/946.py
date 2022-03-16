class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stk = []
        j = 0
        for x in pushed:
            stk.append(x)
            while(stk and stk[-1]==popped[j]):
                stk.pop()
                j+=1
        return j == len(popped)

        pass

obj = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(obj.validateStackSequences(pushed,popped))
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(obj.validateStackSequences(pushed,popped))