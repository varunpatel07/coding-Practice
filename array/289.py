
class Solution:
    def helper(self,board,row,col):
        neighbors = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        livecount = 0
        for i,j in neighbors:
            new_i,new_j = row + i,col+j
            
            if(0<= new_i < len(board) and 0<= new_j < len(board[0]) and abs(board[new_i][new_j])==1):
                livecount+=1
        return livecount


    def gameOfLife(self, board) -> None:
        flip=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                one = self.helper(board,i,j)
                if(board[i][j]==1):
                    if(one<2 or one>3):
                        board[i][j]=-1
                else:
                    if(one==3):
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==-1):
                    board[i][j] = 0
                elif(board[i][j]==2):
                    board[i][j] = 1

board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
    ]
obj = Solution()
print(obj.gameOfLife(board))
print(board)
