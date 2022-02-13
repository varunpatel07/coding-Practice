class Solution:
    def arrayPreorder(self,arr,r):
        if(r>=len(arr)):
            return
        print(arr[r],end=" ")
        self.arrayPreorder(arr,(r*2)+1)
        self.arrayPreorder(arr,(r*2)+2)


    def arrayInorder(self,arr,r):
        if(r>=len(arr)):
            return
        self.arrayInorder(arr,(r*2)+1)
        print(arr[r],end=" ")
        self.arrayInorder(arr,(r*2)+2)


    def arrayPostorder(self,arr,r):
        if(r>=len(arr)):
            return
        self.arrayPostorder(arr,(r*2)+1)
        self.arrayPostorder(arr,(r*2)+2)
        print(arr[r],end=" ")

obj = Solution()
arr = ["A","B","C","D","E","F","G"]
obj.arrayPreorder(arr,0)
print()
obj.arrayInorder(arr,0)
print()
obj.arrayPostorder(arr,0)