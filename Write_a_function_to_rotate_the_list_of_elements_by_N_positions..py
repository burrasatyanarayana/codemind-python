n=int(input())
m=list(map(int,input().split()))
b=int(input())
h=[]
if b<n:
    z=n-b
    for i in range(z,n):
        h.append(m[i])
    for j in range(z):
        h.append(m[j])
    print(*h)
elif n==b or b%n==0:
    print(*m)
elif b>n:
    a=b%n
    z=n-a
    for i in range(z,n):
        h.append(m[i])
    
    for j in range(0,z):
        h.append(m[j])
    print(*h)
        

        