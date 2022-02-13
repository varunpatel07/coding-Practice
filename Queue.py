class Queue:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.front=-1
        self.rear=-1
    
    def isEmpty(self) -> bool:
        if(self.front==-1):
        
            return True

        return False

    def isFull(self) -> bool:
        if((self.rear+1)%self.size==self.front):
            return True
        
        return False

    def enQueue(self,val) -> None:
        if(self.isFull()):
            print("Queue is Full")
            return
        else:
            if(self.isEmpty()):
                self.front= self.rear = 0
                self.arr[self.rear]=val
            else:
                self.rear=(self.rear+1)%self.size
                self.arr[self.rear] = val
                
    
    def deQueue(self) -> int:
        if(self.isEmpty()):
            print("Queue is Empty")
            return None
        val=None
        if(self.front==self.rear):
            val=self.arr[self.rear]
            self.front=self.rear=-1
        else:
            val=self.arr[self.front]
            self.front=(self.front+1)%self.size
        return val

    def __str__(self) -> str:
        
        return str(self.arr)
        
if(__name__=="__main__"):
    obj=Queue(3)
    obj.enQueue(1)
    print(obj)
    obj.enQueue(2)
    print(obj)
    obj.enQueue(3)
    print(obj)
    obj.enQueue(4)
    print(obj.deQueue())
    print(obj.deQueue())
    obj.enQueue(5)
    print(obj)
    obj.enQueue(8)
    print(obj)
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj.deQueue())
    print(obj)