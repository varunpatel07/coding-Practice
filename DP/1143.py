class Solution:
    def helper(self,s,r,i,j,aux):
        if(i>=len(s) or j>=len(r)):
            return 0 
        if((i,j) not in aux):
            if(s[i] == r[j]):
                aux[(i,j)]  = self.helper(s,r,i+1,j+1,aux)+1
            else:
                aux[(i,j)]  = max(self.helper(s,r,i+1,j,aux),self.helper(s,r,i,j+1,aux))
        return aux[(i,j)]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        aux = {}
        #return self.helper(text1,text2,0,0,aux)
        return self.longestCommonSubsequenceDP(text1,text2)
    
    def longestCommonSubsequenceDP(self,s,t):
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]

        for i in range(len(t)-1,-1,-1):
            for j in range(len(s)-1,-1,-1):
                if(t[i] == s[j]):
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]        
obj = Solution()
text1 = "abcdef"
text2 = "acs"
print(obj.longestCommonSubsequence(text1 , text2))