n=int(input())
m=list(map(int,input().split()))
d=0
k=0
for i in range(len(m)-1):
    if m[i]<m[i+1]:
        k+=1
    else:
        d+=1
if len(m)-1==k:
    print('yes')
else:
    print('no')