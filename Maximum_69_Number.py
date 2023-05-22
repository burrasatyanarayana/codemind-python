n=input()
v=list(n)
m=[]
for i in v:
    f=int(i)
    m.append(f)
for i in range(len(m)):
    if m[i]==6:
        m[i]=9
        break
for i in m:
    print(i,end='')
    