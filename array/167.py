class Solution:
    def twoSum(self, numbers, target):
        ind = {}
        for index, item in enumerate(numbers):
            if(item in ind):
                return [ind[item] , index+1]
            else:
                ind[target-item] = index+1
            
            pass
        pass
obj = Solution()
arr = [2,3,4]
t = 6
a="hello"
a.re
print(obj.twoSum(arr,t))
            
        