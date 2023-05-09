z,j=map(int,input().split())
k=str(z)
a=[]
d=''
v=''
for i in k:
    c=int(i)
    a.append(c)
g=a[0:j:1]
h=a[-1:-j-1:-1]
u=h[::-1]
for i in g:
    d+=str(i)
for i in u:
    v+=str(i)
x=int(d)
y=int(v)
print(abs(x-y))


    