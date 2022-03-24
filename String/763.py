"""
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Input: s = "eccbbbbdec"
Output: [10]
"""
class Solution:
    def partitionLabels(self, s: str):
        lastPos = {}
        for idx,chr in enumerate(s):
            lastPos[chr] = idx
        
        end = 0
        partSize = 0
        result = []
        for i in range(len(s)):
            partSize+=1
            end = max(end,lastPos[s[i]])
            if(i == end):
                result.append(partSize)
                partSize = 0
        return result



obj = Solution()
s = "ababcbacadefegdehijhklij"
print(obj.partitionLabels(s))
s = "eccbbbbdec"
print(obj.partitionLabels(s))