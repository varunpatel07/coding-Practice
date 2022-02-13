class Solution:
    def selectionSort(self,arr):
        for i in range(len(arr)):
            min_idx=i
            for j in range(i+1,len(arr)):
                if(arr[min_idx] > arr[j]):
                    min_idx = j
            arr[i],arr[min_idx] = arr[min_idx] , arr[i]

obj=Solution()
arr=[10,5,-14,56,12,98,0]
obj.selectionSort(arr)
print(arr)