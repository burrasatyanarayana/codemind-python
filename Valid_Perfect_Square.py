def sqr(k):
    z=k**0.5
    x=int(z)
    y=x**2
    if y==k:
        return True
    else:
        return  False
n=int(input())
for i in range(n):
    k=int(input())
    h=sqr(k)
    print(h)