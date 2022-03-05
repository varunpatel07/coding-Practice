"""Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4."""


class Solution:
    def helper(self,nums,i,cache={}):
        if(i<0):
            return 0
        if(i in cache):
            return cache[i]
        cache[i] = max(self.helper(nums,i-2)+nums[i],self.helper(nums,i-1))
        return cache[i]

    def rob(self, nums) -> int:
        print(self.helper(nums,len(nums)-1))
        return self.dp(nums)

    def dp(self,nums):
        n = len(nums)
        dp = [0] * (n)
        dp[1] = max(nums[1],nums[0])
        dp[0] = nums[0]
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        print(dp)
        
        return dp[-1]
        

obj = Solution()
print(obj.rob([2,7,9,3,1]))



