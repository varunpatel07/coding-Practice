import sys


tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    s = 0
    evnmin = sys.maxsize
    oddmax  = -sys.maxsize
    for i in range(n):
        if(i%2==0):
            evnmin = min(evnmin,abs(arr[i]))
            s += abs(arr[i])
        else:
            oddmax = max(oddmax,abs(arr[i]))
            s-= abs(arr[i])
    print(s - (2*evnmin) + (2*oddmax))
