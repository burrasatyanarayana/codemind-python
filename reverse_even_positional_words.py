n=input().split(' ')
l=list(n)
p=[]
h=0
for i in l:
    if h%2==0:
        z=i[::-1]
        p.append(z)
    else:
        p.append(i)
    h+=1
print(*p)