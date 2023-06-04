n=int(input())
a=0
b=1
l=[]
l.append(a)
l.append(b)
for i in range(n+2):
    c=a+b
    a,b=b,c
    l.append(c)
    if c>n:
        break
z=l[-1]
y=l[-2]
f=n-y
g=z-n
if f>g:
    print(z)
elif f==g:
    print(y,z)
else:
    print(y)