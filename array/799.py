"""
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if(poured==0):
            return 0
        arr = [[float(0)]*(query_glass+2) for _ in range(query_row+2)]
        arr[0][0] = poured
        for i in range(query_row+1):
            j = 0
            while(j<=query_glass and j<=i):
                if(arr[i][j]>1):
                    remain = arr[i][j] - 1
                    arr[i][j] = 1
                    arr[i+1][j] += remain/2
                    arr[i+1][j+1] += remain/2
                j+=1
        return round(float(arr[query_row][query_glass]),6)
        
        pass

obj = Solution()
poured = 1
query_row = 1
query_glass = 1
print(obj.champagneTower(poured,query_row,query_glass))
poured = 2
query_row = 1
query_glass = 1
print(obj.champagneTower(poured,query_row,query_glass))
poured = 100000009
query_row = 33
query_glass = 17
print(obj.champagneTower(poured,query_row,query_glass))
