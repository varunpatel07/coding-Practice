"""
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

"""

class Solution: 
    def helper(self,matrix,i,j,store):
        if(i>=len(matrix) or j>=len(matrix[0])):
            return 0
        if((i,j) not in store):
            #check how many square we can make using adjecent places
            if(matrix[i][j]=="1"):
                a= self.helper(matrix,i+1,j,store)
                b = self.helper(matrix,i,j+1,store)
                c = self.helper(matrix,i+1,j+1,store)
                store[(i,j)] = min(a,b,c) + 1
            else:
                store[(i,j)] = 0
        
        return store[(i,j)]
    def maximalSquare(self, matrix) -> int:
        a = 0 
        store = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a = max(a,self.helper(matrix,i,j,store))
        return a*a
    
    def maxSquaredp(self,mat):
        dp = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
        maxc = 0
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if(mat[i][j]=='1'):
                    dp[i][j] = min([dp[i+1][j],dp[i][j+1],dp[i+1][j+1]]) + 1
                    maxc = max(maxc,dp[i][j])
        return maxc*maxc


        pass

matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
            ]
obj = Solution()
print(obj.maximalSquare(matrix))
print(obj.maxSquaredp(matrix))