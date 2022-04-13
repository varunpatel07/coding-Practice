class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0]*n for _ in range(n)]
        
        
        
        row = 0
        col = 0
        max_row = n
        max_col = n
        val = 1
        while(row<max_row):
            for i in range(col,max_col):
                matrix[row][i] = val
                val+=1
            for i in range(row+1,max_row):
                matrix[i][max_col-1] = val
                val+=1
            for i in range(max_col-2,col-1,-1):
                matrix[max_row-1][i] = val
                val+=1
            for i in range(max_row-2,row,-1):
                matrix[i][col] = val
                val+=1
            row+=1
            col+=1
            max_col-=1
            max_row-=1        
        return matrix

obj = Solution()
n = 5
ans = obj.generateMatrix(n)
for i in ans:
    print(i)