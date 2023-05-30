import math
def prime(j):
    if j==1 or j==0:
        return False
    z=int(math.sqrt(j))
    for i in range(2,z+1):
        if j%i==0:
            return False
    return True
     
n=int(input())
z=prime(n)
h=0
if z==True:
    s=str(n)
    for i in s:
        d=int(i)
        a1=prime(d)
        if a1==True:
            h+=1
if len(str(n))==h :
    print('Mega Prime')
else:
    print('Not Mega Prime')
    

    