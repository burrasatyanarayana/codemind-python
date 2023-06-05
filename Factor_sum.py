l=list(map(int,input().split(",")))
z=[]
k=[]
for i in range(len(l)):
    d=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            d+=j
    if d in l:
        k.append(l[i])
k.sort()
if len(k)==0:
    print(-1)
else:
    print(*k)