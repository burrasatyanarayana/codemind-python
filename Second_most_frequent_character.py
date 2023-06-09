n=input()
z=[]
k=''
for i in n:
    if i not in k:
        z.append(n.count(i))
        k+=i
s=set(z)
z=list(s)
z.sort(reverse=True)
if len(k)==len(n):
    print(-1)
else:
    h=z[1]
    for i in n:
        if n.count(i)==h:
            print(i)
            break