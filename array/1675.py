"""
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Input: nums = [2,10,8]
Output: 3
"""
from heapq import heapify, heappop, heappush

class Solution:
    def minimumDeviation(self, nums) -> int:
        heap = []
        for x in nums:
            if(x&1):
                heap.append(x*-2)
            else:
                heap.append(-1*x)
        heapify(heap)
        minv, maxv = -max(heap), -heap[0]
        diff = maxv - minv
        while(heap[0]%2==0):
            x = heappop(heap) // 2
            heappush(heap,x)
            minv, maxv = min(minv,-x), -heap[0]
            diff = min(diff,maxv - minv)
        return diff


obj = Solution()
print(obj.minimumDeviation([1,2,3,4]))
print(obj.minimumDeviation([4,1,5,20,3]))
print(obj.minimumDeviation([2,10,8]))

