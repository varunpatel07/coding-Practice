"""Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        map  = {val:i for i,val in enumerate(nums1)}
        op = [0] * len(nums1)
        s = []
        for i in range(len(nums2)-1,-1,-1):
            if(nums2[i] in map):
                while(s and s[-1] < nums2[i]):
                    s.pop()
                if(s):
                    op[map[nums2[i]]] = s[-1]
                else:
                    op[map[nums2[i]]] =  -1    
            s.append(nums2[i])
        return op


obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(obj.nextGreaterElement(nums1,nums2))
