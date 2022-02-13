class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        store = {}
        #to store the frequency of character of string s in a hashmap
        for char in s:
            if(char not in store):
                store[char] = 0
            store[char] +=1 
        
        #to check the character of string t long with their frequency
        for char in t:
            if(char not in store):
                return char
            store[char] -=1
        
        #incase a existing char is added we need to check the frequency of element
        for char,freq in store.items():
            if(freq!=0):
                return char
        