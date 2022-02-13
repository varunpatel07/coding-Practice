"""
Find subarray with given sum | Set 1 (Nonnegative Numbers)

Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number. 
Examples : 

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33
"""
class Solution:
    def subarraySum(self,arr,t):
        start = 0
        curr_sum = arr[0]
        for end in range(1,len(arr)+1):
            
            while(start<end and curr_sum>t):
                curr_sum -= arr[start]
                start+=1
            if(curr_sum == t):
                print(f"{start} {end-1}")
                break
            curr_sum += arr[end]

        pass

obj = Solution()
arr = [3, 4, 2, 3, 10, 3]
t = 33
obj.subarraySum(arr,t)