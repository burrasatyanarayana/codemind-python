def gg(i):
    s=str(i)
    x=s[::-1]
  
    return x
    
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    x=gg(i)
    m.append(x)
for i in m:
    print(int(i),end=' ')