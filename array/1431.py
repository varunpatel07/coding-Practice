class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val=max(candies)
        return [True if val+extraCandies>=max_val else False for val in candies]
        