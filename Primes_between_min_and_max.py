import math
def gg(j):
    x=int(math.sqrt(j))
    for k in range(2,x+1):
        if j%k==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
w=[]
z=max(l)
zz=min(l)
b=l.index(z)
a=l.index(zz)
if a>b:
    for i in range(b,a+1):
        if l[i]==0 or l[i]==1:
            continue
        y=gg(l[i])
        if y==True:
            w.append(l[i])
else:
    for i in range(a,b+1):
        if l[i]==0 or l[i]==1:
            continue
        y=gg(l[i])
        if y==True:
            w.append(l[i])
print(len(w))

    
        