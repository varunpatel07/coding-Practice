class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls=[]
        

    def add(self, key: int) -> None:
        if key not in self.ls:
            self.ls.append(key)
            
        

    def remove(self, key: int) -> None:
        if key in self.ls:
            self.ls.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.ls:
            return True
        return False
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)