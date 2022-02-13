
from collections import deque
from math import dist


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        store = set(wordList)
        wordlen = len(beginWord)
        if(endWord not in store):
            return 0
        q = deque([(beginWord,1)])
        while(q):
        
            val,dist = q.popleft()
            if(val == endWord):
                    return dist
            val = list(val)
            for i in range(wordlen):
                nval = val[:]
                for j in range(ord('a'),ord('z')+1):
                    nval[i] = chr(j)
                    temp = "".join(nval)
                    
                    if(temp in store):
                        store.remove(temp)
                        q.append((temp,dist+1))
            dist+=1
        return 0



        
        
        pass        

obj = Solution()
beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
print(obj.ladderLength(beginWord,endWord,wordList))
        