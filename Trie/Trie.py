class Node:
    def __init__(self,value):
        self.val = value
        self.isword = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node("\0")
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if(i not in curr.children):
                curr.children[i] = Node(i)
            curr = curr.children[i]
        curr.isword = True


        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if(i not in curr.children):
                return False
            curr = curr.children[i]
        return True if curr.isword else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if(i not in curr.children):
                return False
            curr = curr.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");"""