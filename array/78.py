class Solution:
    def subsets(self, nums):     
        def helper(i,path=[]):
            if(i==len(nums)):
                aux.append(path[:])
            else:
                helper(i+1,path)
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
        aux = []
        helper(0)
        return aux

    def subset2(self,nums):
        out = [[]]
        for i in range(len(nums)):
                out.extend([curr +[nums[i]] for curr in out])
        return out 
             
    def subset3(self,nums):
        def help(s,curr=[]):
            out.append(curr[:])

            for i in range(s,len(nums)):
                curr.append(nums[i])
                help(i+1,curr)
                curr.pop()
        out = []
        help(0)
        return out

    def subset4(self,nums):
        """
        This is the most efflicient method using bitmasking
        we can create subset by following the binary numbers.
        if length of array is 2  -[a,b]
        then elements can vary as
        00 - []
        01 - [b]
        10 - [a]
        11 - [a,b]

        but the issue is creating value preceding zero like 01,11 etc.
        the solution is that we create a mask of len n+1 then ignore the msb
        or if we dont want to do the shifiting job then we could start with binary range having len n+1
        """
        n= len(nums)
        out = []
        for i in range(2**n,2**(n+1)):
            bitmask = bin(i)[3:] #return type of bin is string
            out.append([nums[j] for j in range(n) if bitmask[j]=='1'])

        return out
  



obj = Solution()
arr = [1,2,3]
print(obj.subsets(arr))
print(obj.subset3(arr))

