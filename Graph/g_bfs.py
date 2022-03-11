from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}
    def addEdge(self,src,dest):
        if(src not in self.graph):
            self.graph[src] = []    
        self.graph[src].append(dest)
    def BFS(self,strt):

        visit = set()
        q = deque()
        q.append(strt)
        visit.add(strt)
        while(q):
            val = q.popleft()
            print(val)
            if(val in self.graph):
                for vertex in self.graph[val]:
                    if(vertex not in visit):
                        q.append(vertex)
                        visit.add(vertex)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)