n=int(input())
m=list(map(int,input().split()))
z=[]
for i in range(0,n,2):
    for j in range(m[i+1]):
        z.append(m[i])
print(*z)