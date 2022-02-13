arr=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
row=0
column=5
ans=-1
while(row<6 and column>-1):
    if(arr[row][column]==1):
        ans=column
        column-=1
    else:
        row+=1
print(ans)