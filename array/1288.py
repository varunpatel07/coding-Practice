"""
Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
"""
class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        if(len(intervals)==1):
            return 1
        intervals.sort(key = lambda x:(x[0],-x[1]))
        cnt = 0
        l,r = intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]>=l and intervals[i][1]<=r):
                cnt+=1
            else:
                l,r = intervals[i][0],intervals[i][1]
    

        return len(intervals) - cnt

        pass

obj = Solution()
print(obj.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(obj.removeCoveredIntervals([[1,4],[2,3]]))
a=[[1,2],[1,4],[3,4]]
print(obj.removeCoveredIntervals(a))