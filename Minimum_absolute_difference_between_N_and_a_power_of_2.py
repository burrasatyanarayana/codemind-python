n=int(input())
z=[]
for i in range(1,n):
    x=2**i
    z.append(x)
    if x>n:
        break
s=z[-1]
v=z[-2]
h=s-n
g=n-v
if g>h:
    print(h)
else:
    print(g)