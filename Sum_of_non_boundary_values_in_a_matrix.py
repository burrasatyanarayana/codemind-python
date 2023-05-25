a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
q=0
for i in range(a):
    for j in range(b):
        if i!=0 and j!=0 and i!=a-1 and j!=b-1:
            q+=m[i][j]
print(q)