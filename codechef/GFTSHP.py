tc = int(input())
for _ in range(tc):
    x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    i = 0
    while(i<x and arr[i]<=y ):
        cnt+=1
        y-=arr[i]
        i+=1
    if(i<x and arr[i]//2<=y):
        cnt+=1
    print(cnt)
"""3
1 4
5
3 15
4 4 5
3 10
6 7 4
"""