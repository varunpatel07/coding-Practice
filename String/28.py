class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle==""):
            return 0
        if(haystack=="" or len(haystack)<len(needle)):
            return -1
            
        i = 0
        while(i<len(haystack)):
            j = 0
            p = i
            if(haystack[p]==needle[j]):
                while(p<len(haystack) and j<len(needle) and haystack[p]==needle[j]):
                    p+=1
                    j+=1
                if(j==len(needle)):
                    return i
            i = p+1
        return -1

obj = Solution()
s="aaaaa"
u ="baa"
print(obj.strStr(s,u))