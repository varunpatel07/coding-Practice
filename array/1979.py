class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #https://crypto.stanford.edu/pbc/notes/numbertheory/euclid.html(euclidian method)
        minv,maxv=min(nums),max(nums)
        while(minv):
            minv,maxv=maxv % minv, minv
        return maxv
        