tc = int(input())
for _ in range(tc):
    x , y = map(int,input().split())
    a = b = c = 0
    if(y%3==0):
        a = y//3
    elif(y%3==1):
        a = (y//3)+1
        b = 2
    elif(y%3==2):
        a = (y//3)+1
        b = 1
    if(a+b<=x):
        print("YES")
        print(f"{a} {b} {x-a-b}")
    else:
        print("NO")

"""
3
10 30
9 25
8 0
Sample Output 1 
YES
10 0 0
NO
YES
1 3 4"""
        