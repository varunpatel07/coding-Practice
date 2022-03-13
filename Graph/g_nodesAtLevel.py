from collections import deque


class Graph:
    def __init__(self):
        self.graph =  {}
    
    def BFS(self, s, lvl):
        q = deque([s,None])
        cnt = 0
        while(q):
            v = q.popleft()
            if(v==None):
                lvl-=1
                if(q):
                    q.append(None)

                if(lvl==0):
                    return cnt
                cnt = 0
            else:
                if(v in self.graph):
                    q.extend(self.graph[v])
                cnt+= len(self.graph[v])
        return cnt

    
   
    def addEdge(self,s,d):
        if(s not in self.graph):
            self.graph[s] = []
        self.graph[s].append(d)

obj = Graph()   
obj.addEdge(0, 1)
obj.addEdge(0, 2)
obj.addEdge(1, 3)
obj.addEdge(2, 4)
obj.addEdge(2, 5)

level = 2

print(obj.BFS(0, level))

# This code is contributed by Neelam Yadav
