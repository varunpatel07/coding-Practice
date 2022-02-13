
class Solution:
    def isSame(self,s,q):
        for i in range(26):
            if(s[i]!=q[i]):
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        store_1 = [0]*26
        store_2 = [0]*26
        for char in s1:
            store_1[ord(char) - ord('a')]  +=1
        start = 0
        end = 0
        while(end<n):
            store_2[ord(s2[end]) - ord('a')]  +=1
            end+=1

        if(self.isSame(store_1,store_2)):
            return True
        while(end<m):
            #print(end)
            store_2[ord(s2[start]) - ord('a')]  -=1
            store_2[ord(s2[end]) - ord('a')]  +=1
            start+=1
            end+=1
            if(self.isSame(store_1,store_2)):
                return True
        return False




obj = Solution()
a = "ab"
b = "eidbaooo"
print(obj.checkInclusion(a,b))