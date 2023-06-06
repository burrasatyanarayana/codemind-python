n=int(input())
z=str(n)
f=list(z)
k=0
for i in z:
    if z.count(i)==1:
        k+=1
if k==len(z):
    print("Unique Number")
else:
    print("Not Unique Number")