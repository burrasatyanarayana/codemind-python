n,m=map(int,input().split())
l=list(map(int,input().split()))
if m==len(l):
    print(*l)
elif m<len(l):
    s=l[m:len(l):1]
    for i in range(0,m,1):
        s.append(l[i])
    print(*s)