import math
def gg(j):
    x=int(math.sqrt(j))
    for k in range(2,x+1):
        if j%k==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
m=int(input())
w=[]
for i in l:
    if i==1 or i==1:
        continue
    if i<=m:
        y=gg(i)
        if y==True:
            w.append(i)
print(len(w))
        