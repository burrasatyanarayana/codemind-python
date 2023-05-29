n=list(map(str,input().lower().split()))
j=''.join(n)
l=[]
for i in j:
    if j.count(i)==1:
        l.append(i)
l.sort()
s=''.join(l)
print(s)