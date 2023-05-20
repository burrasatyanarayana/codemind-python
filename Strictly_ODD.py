n=int(input())
a=list(map(int,input().split()))
k=0
d=[]
for i in range(1,len(a),2):
    d.append(a[i])
    if a[i]%2==1:
        k+=1
if k==len(d):
    print(True)
else:
    print(False)