n=int(input())
m=list(map(int,input().split()))
c=[]
d=[]
for i in m:
    s=abs(i)
    c.append(s)
c.sort()
for i in c:
    j=i**2
    d.append(j)
print(*d)