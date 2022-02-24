"""
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dp(m,n):
            if(m==0 or n==0):
                return 1
            return dp(m-1,n) + dp(m,n-1)
        return dp(m-1,n-1)

    def dp(self,m,n):
        dp = [[0]*(n) for _ in range(m)]

        for row in range(1,m):
            dp[row][0] = 1
        for col in range(1,n):
            dp[0][col] = 1
    
        for row in range(1,m):
            for col in range(1,n):  
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        print(dp)
        return dp[m-1][n-1]


        

obj = Solution()
m = 3
n = 7
print(obj.uniquePaths(m,n))
print(obj.dp(m,n))
m = 3
n = 2
print(obj.uniquePaths(m,n))
print(obj.dp(m,n))