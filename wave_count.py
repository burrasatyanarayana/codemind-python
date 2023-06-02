n=int(input())
m=list(map(int,input().split()))
l=[]
k=0
h=0
for i in range(0,len(m)-2,2):
    if m[i]<m[i+1] and m[i+1]>m[i+2]:
        k+=1
    else:
        h=1
if  h==1:
    print(-1)
else:
    print(k)

    
    
    