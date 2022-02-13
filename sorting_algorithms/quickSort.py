class Solution:
    def partition(self, arr , low , high):
        #print(id(arr))
        pivot_idx=low
        element = arr[low]
        
        while( low < high):
            while(low< high and arr[low] <= element):
                low+=1
            while( arr[high] > element):
                high-=1
            if(low < high):
                
                arr[low] , arr[high] = arr[high] , arr[low]
    
        arr[high],arr[pivot_idx]=arr[pivot_idx],arr[high]
        
        return high

    def __quickSortInternal(self,arr,low,high):
        if(low < high):
            #print(id(arr))
            p = self.partition(arr, low , high)
            
            self.__quickSortInternal(arr, low , p-1)
            self.__quickSortInternal(arr, p+1 , high)
    def quickSort(self , arr):
        self.__quickSortInternal(arr , 0 , len(arr)-1)
arr = [2,3,4,5,7,0]
obj = Solution()
obj.quickSort(arr)
#obj.partition(arr,0,5)
print(arr)