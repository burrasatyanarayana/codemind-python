import math
def prime(j):
    z=int(math.sqrt(j))
    for i in range(2,z+1):
        if j%i==0:
            return False
    return True
     
n=int(input())
a1=[]
for i in range(2,n):
    s=prime(i)
    if s==True:
        a1.append(i)
a1.sort()
l=0
for i in a1:
    if l==1:
        break
    for p in a1:
        if (i*p)==n:
            print(i,p)
            l=1
            break
if l==0:
    print(-1)