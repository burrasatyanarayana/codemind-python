a,b=map(int,input().split())
m=[]
q=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(b):
    l1=[]
    for j in range(a):
        l1.append(m[j][i])
    s=sorted(l1)
    if(l1==s):
        q+=1
    elif(l1==s[::-1]):
        q+=1
print(q)
        
        
        
    
    
    
    

