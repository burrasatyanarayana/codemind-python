n,m=map(int,input().split())
l=list(map(int,input().split()))
v=0
for i in l:
    if i%m==0:
        v+=1
print(v)
