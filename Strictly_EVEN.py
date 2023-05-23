n=int(input())
m=list(map(int,input().split()))
k=0
l=m[:len(m):2]
for i in l:
    if i%2==0:
        k+=1
if k==len(l):
    print(True)
else:
    print(False)
