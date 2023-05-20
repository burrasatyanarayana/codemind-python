n=int(input())
m=list(map(int,input().split()))
o=[]
k=0
for i in m:
    x=str(i)
    o.append(x)

for i in o:
    if len(i)%2==0:
        k+=1
print(k)