"""
For example, if the price of a stock over the next 7 days were
 [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].

"""
class StockSpanner:

    def __init__(self):
        self.stock = []
        self.span = []

        
        

    def next(self, price: int) -> int:
        while(self.span and self.span[-1][0]<=price):
            self.span.pop()
        res =  len(self.stock) - self.span[-1][1]  if self.span else len(self.stock)+1
        self.span.append((price,len(self.stock)))
        
        self.stock.append(price)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
#[100,80,60,70,60,75,85]
print(obj.next(31))
print(obj.next(41))
print(obj.next(51))
print(obj.next(61))
