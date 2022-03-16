"""
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        stk = []
        remove = set()
        for i in range(len(s)):
            if(s[i]=='('):
                stk.append(i)
            elif(s[i]==')'):
                if(stk):
                    stk.pop()
                else:
                    remove.add(i)
        for i in stk:
            remove.add(i)
        

        return "".join([s[i] for i in range(len(s))  if i not in remove])

obj = Solution()
s = "lee(t(c)o)de)"
print(obj.minRemoveToMakeValid(s))
s = "a)b(c)d"
print(obj.minRemoveToMakeValid(s))
s = "))(("
print(obj.minRemoveToMakeValid(s))