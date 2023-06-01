n=input().lower().split()
m=input().lower().split()
z=[]
for i in m:
    if i in n:
        z.append(i)
print(*z)
        