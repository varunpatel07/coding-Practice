"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)

        def helper(i,curr = []):
            ans.append(curr[:])
            for j in range(i,len(nums)):
                if(j > i and nums[j] == nums[j-1]):
                    continue
                curr.append(nums[j])
                helper(j+1,curr)
                curr.pop()


        ans = []
        helper(0)
        return ans
        pass

obj = Solution()
print(obj.subsetsWithDup([1,2,2]))