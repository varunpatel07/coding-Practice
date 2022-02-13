import sys
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_1=0
        max_2=0
        min_1=min_2=sys.maxsize
        for item in nums:
            #for maximun
            if(item>=max_1):
                max_2=max_1
                max_1=item
            elif(item>max_2 and item<max_1):
                max_2=item
            # for minimum
            
            if(item<=min_1):
                min_2=min_1
                min_1=item
            elif(item<min_2 and item>min_1):
                min_2=item
        return (max_1*max_2)-(min_1*min_2)