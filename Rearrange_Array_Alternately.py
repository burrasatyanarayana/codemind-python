n=int(input())
for i in range(n):
    m=int(input())
    d=[]
    x=list(map(int,input().split()))
    g=0
    for i in range(len(x)-1):
        g+=1
        z=x
        v=max(z)
        d.append(v)
        z.remove(v)
        if len(x)==0:
            break
        b=min(z)
        d.append(b)
        z.remove(b)
        if len(x)==0:
            break
        
    print(*d)