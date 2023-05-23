n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
z=[]
for i in range(len(m)):
    if m[i]<a or m[i]>b:
        z.append(m[i])
if len(z)==0:
    print(-1)
else:
    print(max(z))