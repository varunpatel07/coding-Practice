class Solution:
    def findMaxLength(self, nums) -> int:
        sum_till_now = 0
        maxlen = 0
        store = {}
        for i in range(len(nums)):
            val = nums[i] if nums[i]==1 else -1
            sum_till_now+=val
            
            if sum_till_now not in store:
                store[sum_till_now] = i
            else:
                maxlen = max(maxlen,i-store[sum_till_now])
            print(store)
            if(sum_till_now==0):
                maxlen = i+1
        return maxlen

obj = Solution()
arr = [0,1,1]
print(obj.findMaxLength(arr))