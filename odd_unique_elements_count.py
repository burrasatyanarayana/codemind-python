n=int(input())
m=list(map(int,input().split()))
l=[]
c=0
for i in m:
    if i%2==1:
        l.append(i)
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d.values():
    if i%2==1:
        c+=1
print(c)
    
        