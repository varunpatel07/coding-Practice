class Solution:
    def fp(self,s,r,i,j,c):
        if(i==len(s) or j==len(r)):
            return c
        f = 0
        if(s[i]==r[j]):
            f =  self.fp(s,r,i+1,j+1,c+1)
        c1 = self.fp(s,r,i+1,j,0)
        c2 = self.fp(s,r,i,j+1,0)
        return max([c,f,c1,c2])
        

    def LCS(self,s,r):
        return self.fp(s,r,0,0,0)
        pass

def solve(i, j, count, str1, str2):
        if i >= len(str1) or j >= len(str2):
            return count;
 
        if str1[i] == str2[j]:
            count = solve(i + 1, j + 1, count + 1, str1, str2);

        count1 = solve(i, j + 1, 0,str1, str2);

        count2 = solve(i + 1, j, 0,str1, str2);

        count = max({count, count1,count2});
        return count;
def lcsubstr():
    s = "abcd"
    r = "abcd"
    ans = solve(0,0 , 0, s, r)
    print(ans)

obj = Solution()
s = "abcd"
r = "abcd"
print(obj.LCS(s,r))
lcsubstr()