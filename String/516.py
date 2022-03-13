"""
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

class Solution:

    def helper(self,s,r,i,j,store):
        if(i>=len(s) or j>=len(s)):
            return 0
        if((i,j) in store):
            return store[(i,j)] 
        else:
            if(s[i]==r[j]):
                store[(i,j)] = self.helper(s,r,i+1,j+1,store) + 1
            else:
                store[(i,j)] = max(self.helper(s,r,i,j+1,store),self.helper(s,r,i+1,j,store))
            return store[(i,j)]
    def longestPalindromeSubseq(self, s: str) -> int:
        store = {}
        #return self.helper(s,s[::-1],0,0,store)
        return self.helperdp(s,s[::-1])

    def helperdp(self,s,r):
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-1,-1,-1):
                if(s[i]==r[j]):
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

        pass

obj = Solution()


s = "bbbab"
print(obj.longestPalindromeSubseq(s))
s = "cbbd"
print(obj.longestPalindromeSubseq(s))