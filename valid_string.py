n=input()
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
z=list(d.values())
a=z[0]
k=0
j=0
for i in z:
    if i==a:
        k+=1
    else:
        j+=1
if k==len(z):
    print("Valid String")
elif j==1:
    if j-1==a or j+1==a:
        print("Valid String")
else:
    print("Not Valid")
