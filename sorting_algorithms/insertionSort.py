class Solution:
    def insertionSort(self,arr):
        for i in range(1,len(arr)):
            key=arr[i]
            j = i - 1
            while(i>=0 and key < arr[j]):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key

obj=Solution()
arr = [-43, 82,12,0, 72,91]
obj.insertionSort(arr)
print(arr)