class Solution:
    def reverseWords(self, s: str) -> str:
        #s = s.strip()
        s = s.split(" ")
        print(s)
        ans = [""] * len(s)
        j = len(s)-1
        i= 0 
        while(j>=0):
            if(s[j]!=''):
                ans[i] = s[j]
                i+=1
            j-=1
        return " ".join(ans[:i])


obj = Solution()
print(obj.reverseWords("  hello    world   varun  "))