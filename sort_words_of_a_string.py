def dd(n):
    k=''
    a=list(n)
    for i in a:
        if i not in '!@#$%^&*':
            k+=i
    z=list(k)
    z.sort()
    for i in range(len(n)):
        if a[i] not in '!@#$%^&*':
             a[i]='*'
    j=0
    for i in range(len(a)):
        if a[i]=='*':
            a[i]=z[j]
            j+=1
    return a
n=input().split()
l=[]
for i in n:
    z=dd(i)
    k=''.join(z)
    l.append(k)
print(*l)