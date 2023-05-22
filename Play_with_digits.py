def kk(i):
    g=0
    d=i
    s=str(i)
    if len(s)==1:
        g+=d
    else:
        for j in s:
            g+=int(j)
    return g
        
n=int(input())
e=0
m=list(map(int,input().split()))
for i in m:
    s=kk(i)
    e+=s
print(e)