import math
def gg(j):
    x=int(math.sqrt(j))
    for k in range(2,x+1):
        if j%k==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
w=[]
for i in l:
    if i==0 or i==1:
        continue
    y=gg(i)
    if y==True:
        w.append(i)
print(len(w))

        