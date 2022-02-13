class Link_Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Vertex_Node:
    def __init__(self,data):
        self.val =  data
        self.adj = None
        self.next = None

def getAdjNode(root,val):
    while(root!=None)
    pass

def BFS(n):
    q = [n]
    while(q):
        temp = q.pop()

def visit(g,i,j):
    g[i][j]=2
    if(i>0 and g[i-1][j]==1):
        visit[i-1][j]
    if(j>0 and g[i][j-1]==1):
        visit[i][j+1]
    if(i<len(g)-1 and g[i+1][j]==1):
        visit[i+1][j]
    if(i<len(g[0])-1 and g[i][j+1]==1):
        visit[i][j+1]


def traverse(g):
    cnt = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if(g[i][j]==1):
                cnt+=1
                visit(g,i,j)
    print(cnt)
