a=int(input())
m=list(map(int,input().split()))
w=[]
for i in m:
    a=abs(i)
    s=str(a)
    o=len(s)
    w.append(o)
print(*w)
