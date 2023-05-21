def gg(k,l):
    if len(l)==1:
        return 1
    if len(l)==0:
        return 0
    else:
        c=l
        z=1
        g=1
        for i in l:
            if g==len(l):
                break
            if i>=c[g]:
                z+=1
                
            g+=1
        return z     
n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    x=gg(k,l)
    print(x)