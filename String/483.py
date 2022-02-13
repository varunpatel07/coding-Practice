class Solution:
    def isSame(self,s,p):
        for i in range(26):
            if(s[i]!=p[i]):
                return False
        return True
    
    
    def findAnagrams(self, s: str, p: str):
        len_s = len(s)
        len_p = len(p)
        ans = []
        freq_s , freq_p = [0]*26 , [0]*26
        
        for char in p:
            freq_p[ord('a')-ord(char)]+=1
            
        for char in s[:len_p]:
            freq_s[ord('a')-ord(char)]+=1

        if(self.isSame(freq_s,freq_p)):
            ans.append(0)

        start = 0
        end = len_p
        while(end<len_s):

            
            freq_s[ord('a')-ord(s[start])]-=1
            freq_s[ord('a')-ord(s[end])]+=1
            start+=1
            end+=1
            if(self.isSame(freq_s,freq_p)):
                ans.append(start)
        

        return ans

obj = Solution()
s = "cbaebabacd"
p = "abc"
print(obj.findAnagrams(s,p))
            
        
        