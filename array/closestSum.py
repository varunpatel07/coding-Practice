"""
https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

"""
import sys
class Solution:
    def closestSum(self,arr,x):
        diff = sys.maxsize
        a1 = a2 = 0
        l=0
        h=len(arr)-1
        while(l<h):
            if(abs(x-(arr[l]+arr[h]))<diff):
                diff=abs(x-(arr[l]+arr[h]))
                a1=arr[l]
                a2=arr[h]
            if(arr[l]+arr[h]>x):
                h-=1
            else:
                l+=1
        return [a1,a2]
obj =  Solution()
arr=[1, 3, 4, 7, 10]
x = 15

print(obj.closestSum(arr,x))