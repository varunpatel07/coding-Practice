"""
Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letterLastOccurance = {c: i for i, c in enumerate(s)}
        ans = []
        for i, ch in enumerate(s):
            if ch not in ans:
                while ans and ch<ans[-1] and i<letterLastOccurance[ans[-1]]:
                    ans.pop()
                ans.append(ch)
        return ''.join(ans)

        pass
obj = Solution()
s  = "bcabc"
print(obj.removeDuplicateLetters(s))
s = "cbacdcbc"
print(obj.removeDuplicateLetters(s))