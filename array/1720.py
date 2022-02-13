class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out=[first]+encoded
        for i in range(1,len(out)):
            out[i]=out[i-1]^out[i]
        return out
        