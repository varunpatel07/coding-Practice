import sys
class Solution:
    def deleteAndEarn(self, nums) -> int:
        store = {}
        minv,maxv=sys.maxsize,-sys.maxsize
        for i in nums:
            if(i not in store):
                store[i] = 0
            store[i] += 1
            minv =  min(i,minv)
            maxv = max(i,maxv)
        v1 = 0
        v2 = 0
        res = 0
        for i in range(maxv+1):
            val = store[i] if i in store else 0
            res = max(v1+i*val,v2)
            v1 = v2
            v2 = res
        return res

        pass
obj = Solution()
print(obj.deleteAndEarn([3,4,2]))