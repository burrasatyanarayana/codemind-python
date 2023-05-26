n=int(input())
m=list(map(int,input().split()))
q=[]
for i in m:
    a=abs(i)
    q.append(a)
z=max(q)
    
x=0
l=[]
for i in q:
    if len(str(z))==len(str(i)):
        l.append(i)
for i in l:
    print(i,end=' ')
    