n=int(input())
z=0
while n>0:
    rem=n%10
    if z<rem:
        z=rem
    n=n//10
print(z)