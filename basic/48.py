"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""
from operator import le
from cv2 import randShuffle


class Solution:
    def rotate(self, matrix) -> None:
        left,right = 0, len(matrix) - 1
        while(left<right):
            for i in range(right - left):
                t , b = left, right
                tl = matrix[t][left+i]
                matrix[t][left+ i] = matrix[b - i][left]
                matrix[b - i][left] = matrix[b][right - i]
                matrix[b][right - i] = matrix[t+i][right]
                matrix[t + i][right] = tl
            left+=1
            right-=1
        

            
            
            pass
        pass
obj = Solution()
matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
print(obj.rotate(matrix))
print(matrix)