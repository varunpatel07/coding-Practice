tc = int(input())
for _ in range(tc):
    x = int(input())
    if(x%5!=0):
        print("-1")
    else:
        a = 0
        a = x//10
        x = x%10
        if(x):
            a+=1
        print(a)