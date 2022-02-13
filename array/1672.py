class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for customer in accounts:
            wealth=max(wealth,sum(customer))
        
        return wealth