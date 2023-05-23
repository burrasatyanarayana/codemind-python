a,b=map(int,input().split())
l=[]
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
z=0
v=0
q=0
for i in m:
    z+=1
    if z%2!=0:
        v+=sum(i)
    else:
        q+=sum(i)
print(v,q)
    
        