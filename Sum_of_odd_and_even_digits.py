n=int(input())
h=0
k=0
l=list(map(int,input().split()))
for i in range(1,len(l),2):
    h+=l[i]
for j in range(0,len(l),2):
    k+=l[j]
if (h-k)==0:
    print('YES')
else:
    print('NO')
    