def dead(n):
    if n==1:
        return 0
    elif n==2:
        return 0,1
    else:
        l=[]
        a=0
        b=1
        l.append(a)
        l.append(b)
        while n>=3:
            n=n-1
            c=a+b
            l.append(c)
            a,b=b,c
        return l
n=int(input())
x=dead(n)
print(*x)
    
    