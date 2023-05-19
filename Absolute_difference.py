def ff(k):
    n=0
    for i in range(2,k):
        if k%i==0:
            n=1
            break
    if n==1:
        return True
s=int(input())
j=list(map(int,input().split()))
v=1
m=1
for i in j:
    if ff(i)==True:
        v*=i
    else:
        m*=i
print(v-m)
            
        