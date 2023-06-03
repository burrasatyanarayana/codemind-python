n=int(input())
a=0
b=1
k=0
for i in range (n+2):
    c=a+b
    a,b=b,c
    if c>n:
        break
    if c==n:
        k=1
        break
if k==1:
    print(True)
else:
    print(False)