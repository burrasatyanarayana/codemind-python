n=int(input())
m=list(map(int,input().split()))
c=0
g=0
for i in range(1,n-1):
    if m[i]+m[i-1]!=m[i+1]:
        c=1
        break
if  c==0 and m[n-2]+m[n-3]==m[n-1]  :
    print("yes")
else:
    print("no")
        
            