class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out=[0]*len(indices)

        for i in range(len(indices)):
            out[indices[i]]=s[i]
            
        return "".join(out)