n,m=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
z=[]
for i in l:
    if i in m:
        if i not in z:
            z.append(i)
for i in m:
    if i  in l:
        if i not in z:
            z.append(i)
print(*z)