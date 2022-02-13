class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        cnt = 0
        store = [0]*60
        for song in time:
            store[song%60]+=1
        for i in range(1,30):
            cnt+=store[i]*store[60-i]
        return cnt + (store[0] * (store[0]-1))//2 + (store[30] * (store[30]-1))//2

obj = Solution()
arr=[30,20,150,100,40]
print(obj.numPairsDivisibleBy60(arr))