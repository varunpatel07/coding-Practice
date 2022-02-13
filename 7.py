class Solution:
    def reverse(self, x: int) -> int:
        is_neg = True if x<0 else False
        x = abs(x)
        rev = 0
        while(x):
            #print(x)
            val = x % 10
            rev = (rev*10)+val
            x = x//10
            #print(f"res-{rev}")
        #print(rev)
        return -1*rev if is_neg else rev
        
obj = Solution()
print(obj.reverse(-123))