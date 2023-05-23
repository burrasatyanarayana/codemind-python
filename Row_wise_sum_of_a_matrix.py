a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
z=[]
for i in range(a):
    k=0
    for j in range(b):
        k+=m[i][j]
    z.append(k)
for i in z:
    print(i,end=' ')