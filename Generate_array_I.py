n=int(input())
m=list(map(int,input().split()))
l=[]
for i in range(0,len(m),2):
    for j in range(m[i+1]):
        l.append(m[i])
print(*l)
        