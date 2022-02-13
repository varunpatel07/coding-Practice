"""
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
"""

class Solution:
    def findPairs(self, nums, k: int) -> int:
        store = {}

        for num in nums:
            if(num not in store):
                store[num] = 0
            store[num]+=1


        pair = 0
        for num in store.keys():
            if(k==0):
                if(store[num]>=2):
                    pair+=1
            elif(num+k in store):
                pair+=1
     
        return pair


obj = Solution()
print(obj.findPairs([3,1,4,1,5],0))

