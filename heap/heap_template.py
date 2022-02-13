class Heap:
    def __init__(self,size):
        self.maxsize = size
        self.size = 0
        self.arr = [None] * size
    
    def Heapify(self, r):
        if(r >= self.size or (r*2)+1 >= self.size):
            return
        minv = r
        if((2 * r)+2 <self.size and self.arr[(2*r)+2] < self.arr[minv]):
            minv = (2*r)+2
        if(self.arr[(2*r)+1] < self.arr[minv]):
            minv = (2*r)+1
        if(r!=minv):
            self.arr[r],self.arr[minv] = self.arr[minv], self.arr[r]
            self.Heapify(minv)


    def arrayToHeap(self,arr=[]):
        self.arr = arr
        self.size = len(arr)
        self.maxsize = 2 * len(arr)
        for i in range(self.size//2,-1,-1):
            self.Heapify(i)
        return self.arr
    
    def Insert(self,val):
        if(self.size>=self.maxsize):
            print("full")
            return
        self.arr[self.size] = val
        idx = self.size
        while(idx>0 and self.arr[(idx-1)//2] > self.arr[idx]):
            self.arr[(idx-1)//2],self.arr[idx] = self.arr[idx] , self.arr[(idx-1)//2]
            idx = (idx-1)//2
        self.size+=1

    
    def Delete(self):
        val = self.arr[0]
        self.arr[0] , self.arr[self.size - 1] =  self.arr[self.size - 1] , self.arr[0]
        self.size -=1
        self.Heapify(0)
    
    def display(self):
        print(self.arr[:self.size])


obj =  Heap(5)

#obj.arrayToHeap(arr)
obj.Insert(5)
obj.Insert(1)
obj.Insert(3)
obj.Insert(7)
obj.Insert(-19)
obj.Insert(-19)
obj.display()



