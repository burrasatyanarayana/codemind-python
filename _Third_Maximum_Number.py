n=int(input())
l=list(map(int,input().split()))
if len(l)<=2:
    print(max(l))
else:
    z=set(l)
    g=list(z)
    a=max(g)
    g.remove(a)
    d=max(g)
    g.remove(d)
    print(max(g))