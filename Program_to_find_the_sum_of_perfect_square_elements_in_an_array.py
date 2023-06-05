import math
n=int(input())
m=list(map(int,input().split()))
w=0
for i in m:
    z=math.sqrt(i)
    s=int(z)
    if int(z**2)==s**2:
        w+=i
print(w)
        