n=int(input())
z=str(n)
k=0
j=0
m=0
for i in z:
    if int(i)%2==0:
        k+=1
    elif int(i)%2==1:
        j+=1
    else:
        m+=1
if k==len(z):
    print("Even")
elif j==len(z):
    print("Odd")
else:
    print("Mixed")
