
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        def dp(i):
            if(i>=len(s)):
                return True
            for e in range(i,len(s)):
                if(s[i:e+1] in wordDict and dp(e+1)):
                    return True
            return False
        return dp(0)


    def wordBreakdp(self,s,wordDict):
        dp = [True]*(len(s)+1)

        for i in range(len(s)-1,-1,-1):
            flg  = True
            for e in range(i,len(s)):
                #print(e)
                if(s[i:e+1] in wordDict and dp[e+1]==True):
                    flg = not flg
                    break
            if(flg):
                dp[i] = False
        return dp[0]

                
            

        
        pass
obj = Solution()
s= "catsandog" 
wordDict = set(["cats","dog","sand","and","cat"])

print(obj.wordBreakdp(s,wordDict))
                