class Solution:
    def reverse(self, s , low, high):
        while(low < high):
            s[low] , s[high] = s[high] , s[low]
            low+=1
            high-=1
    def reverseWords(self, s: str) -> str:
        curr= 0
        s=list(s)
        for i in range(len(s)-1):
            if(s[i]==" "):
                self.reverse(s, curr, i-1)
                curr = i+1
        self.reverse(s, curr,len(s)-1)
        return "".join(s)
obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))
print("s'teL ekat edoCteeL tsetnoc")

# this is also a way
a="Let's take LeetCode contest"
print(' '.join(a.split()[::-1])[::-1])