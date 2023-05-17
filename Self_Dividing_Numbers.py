def fod(i):
    f=0
    c=i
    l=[]
    w=[]
    z=str(i)
    for g in z:
        j=int(g)
        l.append(j)
    for h in l:
        if h==0:
            return 'w'
        if c%h!=0:
            f=1
            break
    
    if f==0:
        w.append(c)
    return w

        

n=int(input())
m=int(input())
x=[]
for i in range(n,m+1):
    v=fod(i)
    x.append(v)
for i in x:
    if len(i)==0 or i=='w':
        continue
    print(*i,end=' ')
    