"""
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
output = False

"""
from gc import garbage


class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = {}
        for edge in edges:
            if(edge[0] not in graph):
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if(edge[1] not in graph):
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])
        visit = set()
        
        def helper(curr):
            
            visit.add(curr)
            if(curr == destination):
                return True
            for edge in graph[curr]:
                if(edge not in visit):
                    if(helper(edge)):
                        return True
            return False
        return helper(source)
"""
10
[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
7
5
"""



obj = Solution()
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
"""n = 10
edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5"""
print(obj.validPath(n,edges,source,destination))