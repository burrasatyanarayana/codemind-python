n=int(input())
m=list(map(int,input().split()))
s=n//2
for i in m:
    if m.count(i)>s:
        print(i)
        break