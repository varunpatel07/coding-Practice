# cook your dish here
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(input())
    i = 0
    j = n-1
    while(i<j):
        if(ord(arr[i])>ord(arr[j])):
            arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    c = arr[0]
    flg = True

    for i in range(1,n):
        if(ord(c)<=ord(arr[i])):
            c = arr[i]
        else:
            flg = False

    if(flg):
        print("yes")
    else:
        print("No")

