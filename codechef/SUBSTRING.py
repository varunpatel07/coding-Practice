tc = int(input())
for _ in range(tc):
    x = input()
    res = -1
    currLen = 0
    for i in range(1,len(x)-1):
        if(x[i]!=x[0] and x[i]!=x[-1]):
            currLen+=1
        else:
            currLen = 0
        if(currLen):
            res = max(currLen,res)
    print(res)

"""
Sample Input 1 
2
abcdab
aaa
Sample Output 1 
2
-1
"""
        