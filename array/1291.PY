import math
class Solution:
    def sequentialDigits(self, low: int, high: int):
        ans = []
        val = 1
        inc = 11
        start = 1
        t= 8
        while(val<=high):
            print(start)
            for i in range(t):
                val+=inc
                if(val>=low and val<=high):
                    ans.append(val)
            
            inc = (inc*10)+1
            start = (10*start)+10-t
            val = start
            t-=1
        return ans 

    def sequentialDigits2(self, low: int, high: int):
        ans = []
        s = ["1","2","3","4","5","6","7","8","9"]
        for window in range(len(str(low)),len(str(high))+1):
            for start in range(10-window):
                val = int("".join(s[start:start+window]))
                if(val>=low and val<=high):
                    ans.append(val)
        return ans


obj = Solution()
low = 1000
high = 13000
#print(obj.sequentialDigits(low,high))
print(obj.sequentialDigits2(low,high))