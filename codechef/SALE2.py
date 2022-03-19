tc = int(input())
for _ in range(tc):
    y,x = map(int,input().split())
    ans = 0
    while(y>0):
        if(y>1):
            y-=3
            ans+=x*2
        else:
            y-=1
            ans+=x
    print(ans)