class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if(len(flowerbed)==1 and n==1 and flowerbed[0]==0):
            return True
            
        for i in range(len(flowerbed)):
            print(f"ind {i}")
            if(n==0):
                break
            if(flowerbed[i]==0):
                if((i==0 and flowerbed[i+1]==0) or (i==len(flowerbed)-1 and flowerbed[i-1]==0)):
                    flowerbed[i]=1
                    n-=1
                elif(i>0 and i<len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n-=1
            else:
                if((i>0  and flowerbed[i-1]!=0) or (i<len(flowerbed)-1 and flowerbed[i+1]!=0)):
                    print("neg")
                    return False
            print(n)
        if(n==0):
            return True
        else:
            return False


obj = Solution()
print(obj.canPlaceFlowers([1,0,0,0,1],1))