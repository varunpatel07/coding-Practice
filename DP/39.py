"""
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
from functools import lru_cache


class Solution:
    
    def combinationSum(self, candidates, target: int):
        ans = []
        path=[]
        def dp(i,s):
            if(i>=len(candidates) or s<0):
                return 0 
            if(s==0):
                ans.append(path[:])
                return 0
            dp(i+1,s)
            path.append(candidates[i])
            dp(i,s-candidates[i])
            path.pop()
        dp(0,target)
        return ans
obj = Solution()
candidates = [1,2]
target = 4
print(obj.combinationSum(candidates,target))