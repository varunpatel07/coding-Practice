class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for item in words:
            flg=True
            for i in range(len(item)):
                if(item[i] not in allowed):
                    flg=False
                    break

            if(flg):
                c+=1
        return c