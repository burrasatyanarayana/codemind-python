n=input().split()
g=list(n)
h=''.join(g)
j=list(h)
z=min(j)
x=max(j)
s=0
b=0
for i in j:
    if z==i:
        s+=1
    elif x==i:
        b+=1
print(z,s,x,b)