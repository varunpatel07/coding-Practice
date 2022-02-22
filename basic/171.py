"""
Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701

Input
"FXSHRXW"
Output
2597
Expected
2147483647
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for num in columnTitle:
            ans = ans*26 + ord(num) -ord("A") +1 
        return ans

obj = Solution()
print(obj.titleToNumber("A"))
print(obj.titleToNumber("AB"))
print(obj.titleToNumber("ZY"))
print(obj.titleToNumber("FXSHRXW"))