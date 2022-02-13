class Solution:
    def reverse(self, arr , low , high):
        while(low < high):
            print(f"{low} {high}")
            arr[low] , arr[high] = arr[high] , arr[low]
            low+=1
            high-=1

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k % len(nums)
        mid = len(nums) - k
        self.reverse(nums , 0 , mid - 1)
        self.reverse(nums, mid ,len(nums)-1)
        self.reverse(nums , 0 , len(nums)-1)
obj= Solution()
arr = [1,2,3,4,5,6,7]
k = 3
obj.rotate(arr , k)
print(arr)
        