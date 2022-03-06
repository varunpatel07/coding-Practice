class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            isChanged=False
            for j in range(len(arr)-1):
                if(arr[j]<arr[j+1]):
                    ischanged=True
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
            if(not isChanged):
                return
obj=Solution()
arr=[8,1,2,3,4,5,6,7]
obj.bubbleSort(arr)
print(arr)