class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dum=set()
        for word in words:
            res=""
            for charc in word:
                res+=morse[ord(charc)-97]
            dum.add(res)
        return len(dum)
                
            
        