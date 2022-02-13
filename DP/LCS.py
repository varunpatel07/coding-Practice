"""
a = [1,2,3,4,5]
subarray =  continous array [2,3,4]
subsequence = non continous array but inn sequence[2,4]
subset = non contious and un sequenced
"""
class Solution:
    def LCS(self,s1,s2,i,j):
        if(i==len(s1) or j == len(s2)):
            return 0
        if(s1[i]==s2[j]):
            return self.LCS(s1,s2,i+1,j+1)+1
        return max(self.LCS(s1,s2,i,j+1),self.LCS(s1,s2,i+1,j))
        

    def LCS_DP(self,s1,s2):
        pass
obj = Solution()
print(obj.LCS("ABCB","DBACB",0,0))