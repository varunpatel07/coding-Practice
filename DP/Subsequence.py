"""
a = [1,2,3,4,5]
subarray =  continous array [2,3,4]
subsequence = non continous array but inn sequence[2,4]
subset = non contious and un sequenced
"""
class Solution:
    def Subsequence(self,s,n,val=[],i=0):
        if(i == n):
            print(val)
            return
        val.append(s[i])
        self.Subsequence(s,n,val,i+1)
        val.pop()
        self.Subsequence(s,n,val,i+1)
obj = Solution()
obj.Subsequence([1,2,3],3)