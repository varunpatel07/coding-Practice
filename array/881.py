"""
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        i = 0
        j = len(people)-1
        ans = 0
        while(i<=j):
            if(people[i]+people[j]<=limit):
                i+=1
                j-=1
            else:
                j-=1
            ans+=1
        return ans

obj = Solution()
people = [1,2]
limit = 3
print(obj.numRescueBoats(people,limit))
people = [3,2,2,1]
limit = 3
print(obj.numRescueBoats(people,limit))
people = [3,5,3,4]
limit = 5
print(obj.numRescueBoats(people,limit))