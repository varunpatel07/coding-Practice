"""
Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""
class Solution:
    def numDecodings(self, s: str) -> int:

        store = set([str(i) for i in range(1,27)])

        def dp(i):
            if(i>=len(s)):
                return 1
            a = 0
            b = 0
            if(s[i] in store):
                a = dp(i+1)
            if(i< len(s)-1 and s[i:i+2] in store):
                print(s[i:i+2])
                b = dp(i+2)
            return a+b
        

        def dpi(s):
            n = len(s)
            dp =[0]*(n+1)
            dp[n] = 1
            for i in range(n-1,-1,-1):
                res = 0
                if(s[i] == 0):
                    dp[i] = 0
                else:
                    res += dp[i+1]
                    if(i<n-1 and s[i:i+2] in store):
                        res += dp[i+2]
                dp[i] = res
            return dp[0]

        return dpi(s)
        pass

obj = Solution()
print(obj.numDecodings("27"))
print(obj.numDecodings("226"))
print(obj.numDecodings("06"))