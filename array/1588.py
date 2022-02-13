class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        ans=0
        for i in range(1,len(nums)+1,2):
            for j in range(0,len(nums)-i+1):
                ans+=sum(nums[j:j+i])
        return ans
