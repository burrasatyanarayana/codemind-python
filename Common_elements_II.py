n,m=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
z=[]
for i in l:
    if i not in m:
        if i not in z:
            z.append(i)
for i in m:
    if i not in l:
        if i not in z:
            z.append(i)
print(*z)