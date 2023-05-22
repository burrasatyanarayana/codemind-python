n=int(input())
l=list(map(int,input().split()))
v=[]
m=[]
z=[]
x=len(l)//2
for i in range(x):
    v.append(l[i])
for j in range(x,len(l),1):
    m.append(l[j])
for i in range(len(l)//2):
    z.append(v[i])
    z.append(m[i])
print(*z)
    

