import math
def prime(j):
    z=int(math.sqrt(j))
    for i in range(2,z+1):
        if j%i==0:
            return False
    return True
     
k=int(input())

for i in range(k,1,-1):
    s=prime(i)
    if s==True:
        z=i
        break
for m in range(k,k+10000,1):
    p=prime(m)
    if p==True:
        h=m
        break
a1=abs(k-z)
a2=abs(k-h)
l=[]
if a2<a1:
    print(a2)
else:
    print(a1)
        

