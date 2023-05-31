n=int(input())
l=list(map(int,input().split()))
sum1=[]
for i in range(len(l)):
    if l.count(l[i])==l[i]:
        if l[i] not in sum1:
            sum1.append(l[i])
if len(sum1)==0:
    print(-1)
else:
    d=sum(sum1)/len(sum1)
    print("%.2f"%d)