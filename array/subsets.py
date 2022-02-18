class Solution:
    def subsets(self, nums):

        def helper(i,path=[]):
            aux.append(path[:])
            for j in range(i,len(nums)):
                path.append(nums[j])
                helper(j+1,path)
                path.pop()
        aux = []
        helper(0)
        return aux

obj = Solution()
print(obj.subsets([1,2,3]))