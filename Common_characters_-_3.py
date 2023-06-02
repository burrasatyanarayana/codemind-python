n=input().lower().split()
g=n[0]
x=n[1:]
k=''
for i in range(len(g)):
    s=0
    for j in range(len(x)):
        z=x[j]
        if g[i] in z:
            s+=1
    if s==len(x):
        k+=g[i]
if len(k)==0:
    print(-1)
else:
    h=list(k)
    print(min(h))
