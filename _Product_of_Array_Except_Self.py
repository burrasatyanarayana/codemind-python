n=int(input())
l=list(map(int,input().split()))
w=1
for i in l:
    w*=i
g=[]   
for i in range(n):
    s=w//l[i]
    g.append(s)
print(*g)
    