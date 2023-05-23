n=int(input())
m=list(map(int,input().split()))
a=int(input())
o=0
s=[]
for i in range(len(m)):
    o+=m[i]
    if m[i]==a:
        break
print(o)