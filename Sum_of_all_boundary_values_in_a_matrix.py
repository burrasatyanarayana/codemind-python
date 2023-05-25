a,b=map(int,input().split())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
q=0
for i in range(a):
    for j in range(b):
        if i==0 or j==0 or i==a-1 or j==b-1:
            q+=m[i][j]
        
print(q)