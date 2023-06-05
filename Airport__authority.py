n=int(input())
m=[]
a=0
for i in range(n):
    k=int(input())
    m.append(k)
y=int(input())
for i in m:
    if i<=y:
        a+=1
    else:
        a+=2
print(a)
        