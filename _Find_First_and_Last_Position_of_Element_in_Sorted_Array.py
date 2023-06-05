n=int(input())
m=list(map(int,input().split()))
z=int(input())
if z not in m:
    print("-1 -1")
else:
    s=m.index(z)
    for i in range(len(m)-1,-1,-1):
        if m[i]==z:
            k=i
            break
    print(s,k)
