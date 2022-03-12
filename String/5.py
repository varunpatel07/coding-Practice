"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            l = max(self.expandWindow(s,i,i),self.expandWindow(s,i,i+1))
            if(l>end-start):
                start = i - ((l - 1)//2)
                end = i + (l//2)
        return s[start:end+1]
    def expandWindow(self,s,left,right):
        if(s==None or left>right):
            return 0
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return right - left - 1

obj = Solution()
print(obj.longestPalindrome("babad"))
print(obj.longestPalindrome("cbbd"))