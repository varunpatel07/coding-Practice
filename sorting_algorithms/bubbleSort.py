class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            isChanged=False
            for j in range(len(arr)-1-i):
                if(arr[j]>arr[j+1]):
                    isChanged=True
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
            if(not isChanged):
                return
obj=Solution()
arr=[3,2,1]
obj.bubbleSort(arr)
print(arr)