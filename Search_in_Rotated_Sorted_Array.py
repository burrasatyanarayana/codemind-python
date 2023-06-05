n=int(input())
m=list(map(int,input().split()))
a=int(input())
if a not in m:
    print(-1)
else:
    z=m.index(a)
    
    print(z)