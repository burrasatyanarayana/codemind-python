n=int(input())
m=list(map(int,input().split()))
z=m
k=0
a=[]
for i in range(len(m)):
    for j in range(len(m)):
        if z[i]>m[j]:
            k+=1
    a.append(k)
    k=0
print(*a)
        