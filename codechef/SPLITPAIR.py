tc = int(input())
for _ in range(tc):
    x = input()
    evn = 0
    odd = 0
    for i in range(len(x)-1,-1,-1):
        if(int(x[i])!=0 and int(x[i])%2==0):
            evn+=1
        elif(int(x[i])!=0 and int(x[i])%2!=0):
            odd+=1
    if(int(x[len(x)-1])%2==0):
        if(evn>=2):
            print("yes")
        else:
            print("No")
    else:
        if(odd>=2):
            print("yes")
        else:
            print("No")