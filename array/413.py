class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        dp = [0] * len(nums)
        for i in range(2,len(nums)):
            if(nums[i] - nums[i-1] == nums[i - 1] - nums[i-2]):
                dp[i] = 1 + dp[i-1]
        return sum(dp)
        pass

obj = Solution()
print(obj.numberOfArithmeticSlices([1,2,3,4]))
print(obj.numberOfArithmeticSlices([1]))