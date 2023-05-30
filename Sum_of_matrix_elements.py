n=int(input())
m=int(input())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
h=0
for i in m:
    h+=sum(i)
print(h)