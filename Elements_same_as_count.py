n=int(input())
m=list(map(int,input().split()))
o=0
h=0
s=[]
for i in range(len(m)):
    if m[i]==m.count(m[i]):
        if m[i] not in s:
            s.append(m[i])
            h+=1
if h==0:
    print(-1)
else:
    print(*s)