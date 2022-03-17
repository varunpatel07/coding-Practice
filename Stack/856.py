class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for i in s:
            if(i=='('):
                stk.append(0)
            else:
                val =  stk.pop()
                stk[-1] += max(val*2,1)
        return stk[-1]
        