class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        end = len(matrix[0]) - 1
        for row in range(len(matrix)):
            if(matrix[row][0]>target):
                return False
            if(matrix[row][0]<=target and matrix[row][end]>=target):
                i = 0
                j = end
                while(i<=j):
                    mid = (i+j)//2
                    if(matrix[row][mid]==target):
                        return True
                    if(matrix[row][mid] > target):
                        j = mid - 1
                    else:
                        i = mid + 1
                        
        return False

obj = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(obj.searchMatrix(matrix,target))
