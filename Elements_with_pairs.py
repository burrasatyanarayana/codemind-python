n=int(input())
l=list(map(int,input().split()))
k=0
if len(l)%2==1:
    l.append(0)
print(*l)