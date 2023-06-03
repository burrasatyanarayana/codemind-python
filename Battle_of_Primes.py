import math
def gg(j):
    if j==0 or j==1:
        return False
    x=int(math.sqrt(j))
    for i in range(2,j):
        if j%i==0:
            return False
    return True
n=int(input())
m=int(input())
z=m+n
for i in range(z+1,z+10000):
    s=gg(i)
    if s==True:
        a=i-z
        print(a)
        break