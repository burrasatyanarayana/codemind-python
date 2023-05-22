n=int(input())
m=list(map(int,input().split()))
z=m[::-1]
x=0
for i in range(len(m)):
    if z[i]>0:
        x+=2**i
print(x)