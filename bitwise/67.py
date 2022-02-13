class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j=len(a)-1,len(b)-1
        c=0
        ans=""
        
        while(i>=0 and j >=0):
            res = c + int(a[i]) + int(b[j])
            #print(f"res {res} ans={ans} carry {c}")
            if(res==3):
                ans = "1"+ans
                c=1
            if(res==2):
                ans = "0"+ans
                c=1
            if(res==1):
                ans = "1"+ans
                c=0
            if(res==0):
                ans = "0"+ans
                c=0
            i-=1
            j-=1
        print(f"carry {c} ans={ans}")
        while(i>=0):
            res = c + int(a[i])
            if(res==2):
                ans = "0"+ans
                c=1
            if(res==1):
                ans = "1"+ans
                c=0
            if(res==0):
                ans = "0"+ans
                c=0      
            i-=1
        #print(f"carry {c} ans={ans}")    
        while(j>=0):
            res = c  + int(b[j])
            if(res==2):
                ans = "0"+ans
                c=1
            if(res==1):
                ans = "1"+ans
                c=0
            if(res==0):
                ans = "0"+ans
                c=0 
            j-=1
        #print(f"carry {c} ans={ans}")
        if(c!=0):
            ans="1"+ans
        #print(f"carry {c} ans={ans}")
        return ans
        
obj = Solution()
print(obj.addBinary("1010","1011"))