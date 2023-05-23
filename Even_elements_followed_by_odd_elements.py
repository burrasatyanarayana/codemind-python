n=int(input())
m=list(map(int,input().split()))
k=[]
for i in range(len(m)):
    if m[i]%2==0:
        k.append(m[i])
for i in range(len(m)):
    if m[i]%2!=0:
        k.append(m[i])
print(*k)
