tc = int(input())
for _ in range(tc):
    n = int(input())
    s = input()
    cnt = 0
    i = 0 
    while(i<n):
        if(i<n-1 and s[i]==s[i+1]):
            i+=2
        else:
            i+=1
        cnt+=1
    print(cnt)
