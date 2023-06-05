n=int(input())
m=list(map(int,input().split()))
d=m[len(m):(len(m)//2)-1:-1]
for i in range(len(m)//2):
    d.append(m[i])
print(*d)