n=int(input())
l=list(map(int,input().split()))
o=0
if n%2!=0:
    x=l[:(len(l)//2):]
else:
    x=l[:len(l)//2:]
a=sum(x)
v=l[len(x):n:]
b=sum(v)
print(abs(a-b))