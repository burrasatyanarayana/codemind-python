n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    m=list(map(int,input().split()))
    for i in m:
        s.append(i)
    s.sort()
    print(*s)