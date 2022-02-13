

class Solution:
    def merge(self, arr , low , mid , high):
        size= (mid - low) +1
        aux = [None] * size
        k = 0
        i = low
        while( i <= mid):
            
            aux[k] = arr[i]
            i+=1
            k+=1
        k=low
        i=0
        j=mid+1
        while(j<= high and i < size):
            #print(f"{i} {j}")
            if(arr[j] < aux[i]):
                arr[k] = arr[j]
                j+=1
            else:
                arr[k] = aux[i]
                i+=1
            k+=1
        while(j <= high):
            arr[k] = arr[j]
            j+=1
            k+=1
        while(i < size):
            #print(f" {arr} {i} {k}")
            arr[k] = aux[i]
            i+=1
            k+=1
    
    def __mergeSortInternal(self , arr , low , high):
        if(high > low):
            #print(f"callled {low} {high}")
            mid = low + (high - low) // 2
            self.__mergeSortInternal(arr , low , mid )
            self.__mergeSortInternal(arr , mid+1 , high )
            self.merge(arr , low , mid , high)
            

    def mergeSort(self,arr):
        self.__mergeSortInternal(arr , 0 , len(arr)-1)
    
    def mergeSortV2(self,arr):
        if(len(arr)>1):
            mid= len(arr)//2
            left= self.mergeSortV2(arr[:mid])
            right = self.mergeSortV2(arr[mid:])

            i=j=k=0
            while(i<len(left) and j < len(right)):
                if(left[i] < right[j]):
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            while(i < len(left)):
                arr[k] = left[i]
                i+=1
                k+=1
            while(j < len(right)):
                arr[k] = right[j]
                j+=1
                k+=1
        return arr
                

obj=Solution()
arr = [2,3,5,1,67,2,0,-32,6,4]
#obj.mergeSort(arr)
print(obj.mergeSortV2(arr))
print(arr)

