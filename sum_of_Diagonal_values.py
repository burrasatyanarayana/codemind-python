a,b=map(int,input().split())
m=[]
n=b-1

for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
q=0
for i in range(a):
    for j in range(b):
        if i==j:
            q+=m[i][j]
        elif j==n :
            q+=m[i][j]
    n=n-1      
print(q)
        
        
        