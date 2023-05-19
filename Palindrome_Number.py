def ff(n):
    z=str(n)
    l=[]
    a=''
    for i in z:
        h=int(i)
        l.append(h)
    x=l[::-1]
    for i in x:
        z=str(i)
        a+=z
    r=int(a)
    if r==n:
        return True
    else:
        return False
p=int(input())
for i in range(p):
    n=int(input())
    z=ff(n)
    print(z)