n=int(input())
m=list(map(int,input().split()))
a=0
for i in m:
    if i==0 or i==1:
        a+=1
if a==n:
    print(True)
else:
    print(False)