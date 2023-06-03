n=int(input())
m=int(input())
k=[]
for i in range(n,m+1):
    z=str(i)
    s=z[::-1]
    if z==s:
        k.append(i)
print(*k)
        