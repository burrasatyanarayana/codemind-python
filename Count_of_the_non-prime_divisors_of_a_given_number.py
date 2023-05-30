import math
n=int(input())
k=[]
l=[]
for i in range(1,n+1):
    if n%i==0:
        k.append(i)
for i in range(2,n+1):
    c=0
    z=int(math.sqrt(i))
    for j in range(2,z+1):
        if i%j==0:
            c=1
            break
    if c==0:
        l.append(i)
for i in l:
    if i in k:
        k.remove(i)

print(len(k))
        