class heap:
    def __init__(self,size):
        self.minHeap = [None]*size
        self.k = size 
        self.cs = 0

    def insert(self,val):
        if(self.cs >= self.k):
            return
        self.minHeap[self.cs] = val
        idx = self.cs
        while(idx>0 and self.minHeap[(idx-1)//2]<self.minHeap[idx]):
            self.minHeap[(idx-1)//2],self.minHeap[idx] = self.minHeap[idx],self.minHeap[(idx-1)//2]
            idx = (idx-1)//2
        self.cs +=1
        print(self.minHeap)
obj = heap(5)
obj.insert(7)
obj.insert(6)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.insert(7)