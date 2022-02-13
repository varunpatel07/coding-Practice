class Solution:
    def __init__(self):
        self.cache = [-1] * 50
    
    def fibonacci(self,n):
        if(n==0 or n==1):
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

    def fibonacciMem(self,n):
        if(n==0 or n==1):
            return n
        if(self.cache[n] != -1):
            return self.cache[n]
        self.cache[n] = self.fibonacciMem(n-1)+self.fibonacciMem(n-2)
        return self.cache[n]
    
    def fibIter(self,n):
        arr = [-1] * (2*n)
        arr[0] = 0
        arr[1] = 1
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        print(arr[n])

obj = Solution()
print(obj.fibonacci(10))
print(obj.fibonacciMem(10))
print(obj.cache)
obj.fibIter(10)