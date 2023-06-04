import math
n=int(input())
m=list(map(int,input().split()))
b=m[0]
for i in range(1,len(m)):
     c=math.lcm(b,m[i])
     b=c
print(c)
    
