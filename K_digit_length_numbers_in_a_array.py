a,b=map(int,input().split())
m=list(map(int,input().split()))
w=[]
for i in m:
    a=abs(i)
    s=str(a)
    if b==len(s):
        w.append(a)
print(len(w))
