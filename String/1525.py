class Solution:
    def numSplits(self, s: str) -> int:
        left = {}
        right = {}
        cnt = 0
        for c in s:
            if(c not in right):
                right[c] = 0
            right[c] +=1
        
        for i in s:
            if(i not in left):
                left[i] = 0
            left[i] +=1
            right[i] -=1
            if(right[i] == 0):
                del right[i]
            
            if(len(left) == len(right)):
                cnt+=1
                
        return cnt