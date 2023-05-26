n=input().split(' ')
z=list(n)
l=[]
for i in z:
    d=list(i)
    c=max(d)
    v=min(d)
    a=ord(c)-ord(v)
    l.append(a)
print(*l)