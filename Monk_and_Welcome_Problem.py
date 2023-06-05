n=int(input())
m=list(map(int,input().split()))
k=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(m[i]+k[i])
print(*a)