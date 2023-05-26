n=int(input())
m=list(map(int,input().split()))
z=min(m)
x=0
for i in m:
    if len(str(z))==len(str(i)):
        x+=1
print(x)
    