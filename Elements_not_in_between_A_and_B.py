n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(len(m)):
    if m[i]<a or m[i]>b:
        k.append(m[i])
if len(k)==0:
    print(-1)
else:
    print(*k)
    
    
    