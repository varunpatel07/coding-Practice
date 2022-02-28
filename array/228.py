"""
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
class Solution:
    def summaryRanges(self, nums):
        ans = []
        start = 0
        end = 0
        while( end<len(nums)):
            win = start+1
            while(win<len(nums) and nums[win] == nums[win-1] + 1):
                end = win
                win += 1

            if(win==start+1):
                ans.append(f"{nums[start]}")
                start = start+1
            else:
                ans.append(f"{nums[start]}->{nums[end]}")
                start = win
            end = start
        return ans

        pass

obj = Solution()
print(obj.summaryRanges([0,1,2,4,5,7]))
print(obj.summaryRanges([0,2,3,4,6,8,9]))
