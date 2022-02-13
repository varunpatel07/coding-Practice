"""
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""
class Solution:
    
    def allPathsSourceTarget(self, graph):
        ans = []
        def helper(i,curr=[]):
            curr.append(i)
            if(i == len(graph)-1):
                ans.append(curr[:])
                return

            for vertex in graph[i]:
                helper(vertex,curr)
                curr.pop()
        helper(0)
        
        return ans
        


obj = Solution()
graph = [[1,2],[3],[3],[]]
print(obj.allPathsSourceTarget(graph))