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
s=gg(n)
if s==True:
    z=str(n)
    a=z[::-1]
    c=int(a)
    f=gg(c)
    if f==True:
        print("circular prime")
    else:
        print("prime but not a circular prime")
if s==False:
    print("not prime")
        
        