n=int(input())
m=list(map(int,input().split()))
d=[]
e=[]
g=[]
m.sort(reverse=True)
for i in range(1,len(m),2):
    g.append(m[i])
    g.append(m[i-1])
if n%2!=0:
    g.append(m[-1])
print(*g)

        