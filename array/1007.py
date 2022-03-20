import sys
class Solution:
    def minDominoRotations(self, tops, bottoms) -> int:
        arr1 = [0]*7
        arr2 = [0]*7
        ans = sys.maxsize
        for i in range(len(tops)):
            arr1[tops[i]]+=1
            arr2[bottoms[i]]+=1
        for i in range(1,7):
            isPossible = True
            if(arr1[i]+arr2[i]>=len(tops)):
                for j in range(len(tops)):
                    if(tops[j]!=i and bottoms[j]!=i):
                        isPossible = False
                        break
                if(isPossible):
                    ans = min(ans,len(tops) - max(arr1[i],arr2[i]))
        if(ans == sys.maxsize):
            return -1
        else:
            return ans

        pass

obj = Solution()
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(obj.minDominoRotations(tops,bottoms))
tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(obj.minDominoRotations(tops,bottoms))