n=set(input().lower().split())
m=set(input().lower().split())
z=''.join(m)
s=''.join(n)
k=''
for i in z:
    if i in s:
        if i not in k:
           k+=i
for i in s:
    if i in z:
        if i not in k:
            k+=i
a=list(k)
a.sort()
d=''.join(a)
print(len(d))