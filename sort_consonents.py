def gg(s):
    k=''
    a=list(s)
    for i in a:
        if i not in 'aeiouAEIOU':
            k+=i
    z=list(k)
    z.sort()
    for i in range(len(s)):
        if a[i] not in 'AEIOUaeiou':
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
    z=gg(i)
    l.append(''.join(z))
print(*l)
