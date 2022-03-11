
"""tc = int(input())
for _ in range(tc):
    n = int(input())
    s = set([i for i in range(1,n+1)])
    i = 0
    while(i*2 < n+1):
        if(i*2 in s):
            s.remove(i*2)
        i+=1
    print(len(s))"""
for n in range(1,101):
    s = set([i for i in range(1,n+1)])
    i = 0
    while(i*2 < n+1):
        if(i*2 in s):
            s.remove(i*2)
        i+=1
    print(f"{n} --> {len(s)}",end="  ")
    if(n%2==0):
        print(n//2)
    else:
        print((n//2)+1)
        
"""tc = int(input())
for _ in range(tc):
    n = int(input())
    s = [True]*(n+1)
    i = 1
    while(i*2 <= n+1):
        if(s[i]==True):
            j = i*2
            while(j<n+1):
                s[j] = False
                j *= 2
        i+=1
    cnt=0
    for i in range(1,n+1):
        if(s[i]):
            cnt+=1
    print(cnt)"""