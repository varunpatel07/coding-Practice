"""tc = int(input())
mod = 998244353

for _ in range(tc):
    ans = 0
    l = int(input())
    c = input()
    for i in range(len(c)):
        for j in range(i,len(c)):
            ans ^= int(c[i:j+1],2)
    print(ans%mod)
    tIME LIMIT EXCEED"""
tc = int(input())
mod = 998244353

for _ in range(tc):
    n = int(input())
    s = input()
    a = [0] * n
    c = 1
    res = 0
    if(s[0]=='1'):
        a[0] = 1

    arr = a[0]
    for i in range(1,n):
        if(s[i]=='1'):
            arr+=(i+1)
        a[i] = arr
        a[i] %=2
    for i in range(n-1,-1,-1):
        if(a[i]==1):
            res+=c
            res = res%mod
        c = c*2
        c = c % mod
    print(res%mod)


"""
3
2
10
3
101
4
1111
1"""