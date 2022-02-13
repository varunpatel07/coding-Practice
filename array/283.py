class Solution:
    def moveZeroes(self, arr):

        curr=0
        i=0
        while(i < len(arr) and curr < len(arr)):
            if(arr[curr] != 0):
                curr += 1
            elif(arr[i]!=0):
                arr[curr] , arr[i] = arr[i] , arr[curr]
                curr+=1
            i+=1

    def moveZeroes2(self, arr):
        curr=0
        ins_pos = 0
        while(curr<len(arr)):
            if(arr[curr]!=0):
                arr[curr] , arr[ins_pos] = arr[ins_pos] , arr[curr]
                ins_pos+=1
            curr+=1
        


obj = Solution()
arr = [1,1,0,2]
#obj.moveZeroes(arr)
obj.moveZeroes2(arr)
print( arr )