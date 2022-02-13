class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while(True):
            while(num):
                res += num%10
                num = num//10
            if(res//10 == 0):
                return res
            else:
                num = res
                res = 0
obj = Solution()
print(obj.addDigits(0))