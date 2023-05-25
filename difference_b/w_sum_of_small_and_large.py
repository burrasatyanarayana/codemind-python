n=input()
n=n.split(' ')
z=list(n)
a=[]
b=[]
for i in z:
    a.append(max(i))
    b.append(min(i))
k=0
for i in a:
    k+=ord(i)
for j in b:
    k-=ord(j)
print(abs(k))
    