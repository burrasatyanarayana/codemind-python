a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
z=[]
d=[]
for i in range(a):
    q=0
    h=0
    s=0
    u=0
    for j in range(b):
        h+=1
        if h==3:
            break
        if m[i][j]<m[i][j+1]:
            q=1
        elif m[i][j]>m[i][j+1]:
            u=1
        else:
            s=1
    if s==0 and q==0:
        z.append(u)
    elif s==0 and u==0:
        z.append(q)
print(len(z))




