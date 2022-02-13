from functools import lru_cache



class Solution:
   

    def maximumScore(self, nums, multiplier) -> int:
        @lru_cache()
        def helper(m,left):
            if(m >= len(multiplier)):
                return 0
            right = len(nums)-(m-left) - 1
            choice_1 = multiplier[m]*nums[left]+(helper(m+1,left+1))
            choice_2 = multiplier[m]*nums[right]+(helper(m+1,left))
            return max(choice_1,choice_2)
        return helper(0,0)


    def maxScore(self,nums,multiplier):
        dp = [[0]*(len(multiplier)+1) for _ in range(len(multiplier)+1)]
        for i in range(len(multiplier)-1,-1,-1):
            for j in range(i,-1,-1):
                right = len(nums) - (i-j) - 1
                op1 = (multiplier[i] * nums[j]) + dp[i+1][j+1]
                op2 = multiplier[i] * nums[right] + dp[i+1][j]
                dp[i][j] = max(op1,op2)
        
        return dp[0][0]

obj = Solution()
print(obj.maxScore([1,2,3],[3,2,1]))