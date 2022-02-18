"""
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(len(num)==k):
            return "0"
        
        s = []
        for numb in num:
            while(s and s[-1]>numb and k):
                k-=1
                s.pop()
            s.append(numb)
        if(k>0):
            s = s[:-k]
        return "".join(s).lstrip("0") or "0"
        pass
obj = Solution()
a = "54123"
b = "10200"
c = "10"
print(obj.removeKdigits(a,3))
print(obj.removeKdigits(b,1))
print(obj.removeKdigits(c,2))