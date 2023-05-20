n=int(input())
a=list(map(int,input().split()))
k=0
for i in a:
    if i%2==0:
        k+=1
if k==len(a):
    print(True)
else:
    print(False)