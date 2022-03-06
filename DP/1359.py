class Solution:
    def countOrders(self, n: int) -> int:
        ways=1
        mod=10**9+7
        for i in range(1,n+1):
            ways *= i*(2*i-1)
            ways%=mod

        return ways%mod
