n=int(input())
m=list(map(int,input().split()))
o=0
s=[]
for i in range(len(m)):
    if m[i]%2==0:
        break
    o+=m[i]
print(o)