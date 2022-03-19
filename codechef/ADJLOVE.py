
tc = int(input())
for _ in range(tc):
    x = input()
    arr = list(map(int,input().split()))
    evn = []
    odd = []
    for i in arr:
        if(i%2==0):
            evn.append(i)
        else:
            odd.append(i)
    for item in evn:
        print(item,end=" ")
    for item in odd:
        print(item,end=" ")
