class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=""
        for i in range(0,len(s),numRows+2):
            ans+=s[i]
        for i in range(1,len(s),2):
            ans+=s[i]
        for i in range(2,len(s),numRows+1):
            ans+=s[i]
        
        return ans
obj = Solution()
s="PAYPALISHIRING"
n = 4
print(obj.convert(s,n))