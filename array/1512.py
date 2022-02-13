class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        aux={}
        ans=0
        for i in range(len(nums)):
            if nums[i] not in aux:
                aux[nums[i]]=0
            else:
                aux[nums[i]]+=1
                ans+=aux[nums[i]]
            
        return ans