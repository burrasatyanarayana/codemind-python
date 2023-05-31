import math 
def gg(j):
    x=int(math.sqrt(j))
    for k in range(2,x+1):
        if j%k==0:
            return False
    return True
    
n=int(input())
for i in range(n+1,n+100000,1):
    v=gg(i)
    if v==True:
        y=str(i)
        r=y[::-1]
        c=''.join(r)
        e=int(c)
        if e==i:
            print(e)
            break
        