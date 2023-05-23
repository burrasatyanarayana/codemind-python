n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
o=0
m=[]
for i in range(len(l)):
    if a<=l[i]<=b:
        m.append(l[i])
if len(m)==0:
    print(-1)
else:
    print(max(m))
    