from math import ceil
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        min_banana,max_banana=1,max(piles)
        while(min_banana<max_banana):
            
            mid = (min_banana+max_banana)//2
            print(f"{min_banana} {max_banana} {mid}")
            time_taken = sum(ceil(pile/mid) for pile in piles)
            if(time_taken<=h):
                max_banana = mid
            else:
                min_banana = mid+1
                
        print(min_banana)
      
    

obj = Solution()
obj.minEatingSpeed([30,11,23,4,20],5)