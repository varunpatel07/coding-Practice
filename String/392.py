"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_pointer = 0
        for chr in t:
            if(s[s_pointer]==chr):
                s_pointer+=1
            if(s_pointer==len(s)):
                return True
        return False
        pass

obj = Solution()
s = "abc"
t = "ahbgdc"
print(obj.isSubsequence(s,t))
s = "axc"
t = "ahbgdc"
print(obj.isSubsequence(s,t))