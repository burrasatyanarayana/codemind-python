n=input().lower()
m=input().lower()
a=n.split()
b=m.split()
k=0
for i in a:
    if i in b:
        k+=1
print(k)