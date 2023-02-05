n= input()
i=len(n)
n=int(n)
k=0
z=n
while n!=0:
     r=n%10
     k=k+r**i
     n=n//10
     i-=1
if k==z:
    print("True")
else:
    print("False")