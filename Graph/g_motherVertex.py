class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.graph =  {}
    
    def dfs(self,s,visit):
        if(s not in visit):
            visit.add(s)
        if(s in self.graph):
            for vertex in self.graph[s]:
                self.dfs(vertex,visit)  
        if(len(visit) == self.vertex):
            return True
        else:
            return False

    def addEdge(self,s,d):
        if(s not in self.graph):
            self.graph[s] = []
        self.graph[s].append(d)

    def findMother(self):
        for node in self.graph:
            if(self.dfs(node,set())):
                return node
        pass

# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print ("A mother vertex is " + str(g.findMother()))

# This code is contributed by Neelam Yadav
