"""
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
"""
from functools import lru_cache
import sys

class Solution:
    def minDifficulty(self, jobDifficulty, d: int) -> int:
        n = len(jobDifficulty)
        if(len(jobDifficulty)<d):
            return -1
        @lru_cache(None)
        def helper(index,remainday):
            if(remainday == d):
                return max(jobDifficulty[index:])    
            hardest = 0
            best = sys.maxsize
            for i in range(index,n - (d - remainday )):
                hardest = max(hardest,jobDifficulty[i])
                best = min(best,hardest + helper(i+1,remainday+1))
            return best

        return helper(0,1)

    
obj = Solution()
jobDifficulty = [11,111,22,222,33,333,44,444]

d = 6
print(obj.minDifficulty(jobDifficulty,d))