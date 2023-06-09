n=int(input())
m=list(map(int,input().split()))
x=''
a=[]
for i in m:
    if str(i) not in x:
         a.append(m.count(i))
         x+=str(i)
a.sort(reverse=True)
m.sort()
f=[]
b=''
for i in range(len(a)):
    for j in range(len(m)):
        if a[i]==m.count(m[j]):
            if str(m[j]) not in b:
                 f.append(m[j])
                 b+=str(m[j])
print(*f)