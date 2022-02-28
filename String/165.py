"""
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
"""
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        arr1 = v1.split(".")
        arr2 = v2.split(".")
        for i in range(min(len(arr1),len(arr2))):
            a = int(arr1[i])
            b = int(arr2[i])
            if(a<b):
                return -1
            if(a>b):
                return 1
        return 0
        
        pass
version1 = "1.01"
version2 = "1.001"
obj = Solution()
print(obj.compareVersion(version1,version2))
version1 = "1.0"
version2 = "1.0.0"
print(obj.compareVersion(version1,version2))
version1 = "1.0.1"
version2 = "1"
print(obj.compareVersion(version1,version2))