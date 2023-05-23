a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
z=[]
d=[]
for i in range(b):
    k=0
    for j in range(a):
        k+=m[j][i]
    z.append(k)
for i in range(a):
    q=0
    for j in range(b):
        q+=m[i][j]
    z.append(q)
print(max(z))
