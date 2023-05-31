n=int(input())
m=list(map(int,input().split()))
z=[]
for i in m:
    if m.count(i)==i:
             z.append(i)
if len(z)==0:
    print(-1)
else:
    print(min(z),max(z))