#similar to target sum problem
#brute force approch -> we need to use 4 loops to check all possible solutions (O(n^4))
#optimized approch - > (N^2) we store all possible combination of two array in hashmap and while traversing next two arrays we would check
#if the opposite value is present in array or not.
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        store = {}
        cnt = 0
        for i in nums1:
            for j in nums2:
                if((i+j) not in store):
                    store[i+j] = 0
                store[i+j] += 1
        for i in nums3:
            for j in nums4:
                cnt+= store[-(i+j)] if -(i+j) in store else 0

        return cnt

obj = Solution()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(obj.fourSumCount(nums1,nums2,nums3,nums4))