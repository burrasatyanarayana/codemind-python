a,b=map(int,input().split())
l=[]
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
z=0
v=0
q=0
for i in range(a):
    for j in range(b):
        if m[i][j]%2==0:
            v+=m[i][j]
        else:
            q+=m[i][j]
print(v,q)
    