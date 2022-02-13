class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        out=[]
        for i in range(n):
            out+=[nums[i],nums[n+i]]
        return out
        