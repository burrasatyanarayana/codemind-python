n=int(input())
m=0
for i in range (n+1,n+1000,1):
    x=str(i)
    s=x[::-1]
    if s==x:
        j=i
        break
for t in range (n-1,1,-1):
    d=str(t)
    h=d[::-1]
    if h==d:
        m=t
        break
q=abs(j-n)
a=abs(n-m)
if q==a:
    print(m,j)
elif q>a:
    print(m)
else:
    print(j)