"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        curr = strs[0]
        l = len(strs[0])
        if(curr==""):
            return ""
        for item in strs[1:]:
            i = 0
            while(i<len(item) and i<len(curr) and item[i] == curr[i]):
                i+=1
            l = min(l,i-1)
            if(i==0 or item==""):
                return ""
        return curr[:l+1]
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
print(obj.longestCommonPrefix(["dog","racecar","car"]))
print(obj.longestCommonPrefix(["a","ab"]))
#print(obj.longestCommonPrefix([]))
a = ["flower","flow","flight"]
print(a[1].indexOf(a[0]) )