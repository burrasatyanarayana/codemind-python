n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
sum1=0
for i in range(len(l)):
    if  a<=l[i]<=b:
        sum1+=l[i]
print(sum1)
