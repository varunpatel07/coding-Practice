class Node:
    def __init__(self,value):
        self.value = value
        self.is_word = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node("\0")
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for chr in word:
            if(chr not in curr.children):
                curr.children[chr] = Node(chr)
            curr = curr.children[chr]
        curr.is_word = True


    def local_search(self, word, curr, idx) -> bool:

        for i in range(idx,len(word)):
            if(word[i]=="."):
                for node,val in curr.children.items():
                    if(self.local_search(word,val,i+1)):
                        return True
                return False
            else:
                if(word[i] not in curr.children):
                    return False
                curr = curr.children[word[i]]
        return curr.is_word
    
    def search(self, word: str) -> bool:
        return self.local_search(word,self.root,0)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
print(obj.search(".at"))
# param_2 = obj.search(word)