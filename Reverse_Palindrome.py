n=int(input())
while 1 :
    x=str(n)
    s=x[::-1]
    a=int(x)
    b=int(s)
    q=a+b
    d=str(q)
    e=d[::-1]
    if d==e:
        print(d)
        break
    else:
        n=q
        