class OrderedStream:

    def __init__(self, n: int):
        self.res=[None]*n
        self.ptr=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.res[idKey]=value
        if(idKey>self.ptr):
            return []
        else:
            while(self.ptr<len(self.res) and self.res[self.ptr] is not None):
                self.ptr+=1
        return self.res[idKey:self.ptr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)