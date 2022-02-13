"""
Input: nums = [1,1,1], k = 2
Output: 2

5,5,-5, 5    k = 5
0,5,10,5,10
cnt = 2
0 : 1
5 : 1
10 : 1

"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        store = {}
        sumv = 0
        cnt = 0
        store[0] = 1
        for num in nums:
            sumv += num
            if(sumv - k in store):
                cnt += store[sumv-k]
            if(sumv not in store):
                store[sumv] = 0
            store[sumv] += 1
        return cnt

obj = Solution()

print(obj.subarraySum([1,1,1],2))