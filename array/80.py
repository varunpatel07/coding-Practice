"""Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""
class Solution:
    def removeDuplicates(self, nums) -> int:
        if(len(nums)<=2):
            return 0
        start = 2
        for end in range(2,len(nums)):

            if(nums[start-2]!=nums[end]):
                nums[start] = nums[end]
                start+=1
        print(nums)
        return start         


obj = Solution()
nums = [1,2,2]
print(obj.removeDuplicates(nums))
print(nums)