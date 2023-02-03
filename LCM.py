n,m=map(int,input().split())
 
if n>m:
    bignumber=n
else:
    bignumber=m
s=bignumber
while True:
    if bignumber%n==0 and bignumber%m==0:
        print(bignumber)
        break
    else:
        bignumber=bignumber+s