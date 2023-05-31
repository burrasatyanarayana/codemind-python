n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
sum1=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        sum1.append(l[i])
if len(sum1)==0:
    print(-1)
else:
    print(min(sum1))