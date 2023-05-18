def dead(n):
    if n==1:
        return True
    else:
        l=[]
        a=0
        b=1
        k=0
        while True:
            k+=1
            if k==n:
                break
            
            c=a+b
            l.append(c)
            a,b=b,c
        for i in l:
            if i==n:
                return True
    return False
n=int(input())
v=n
x=dead(n)
print(x)


    