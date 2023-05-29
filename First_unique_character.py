n=list(map(str,input().lower().split()))
j=''.join(n)
s=''
for i in j :
    if j.count(i)==1:
        s+=i
        break
if len(s)==0:
    print(-1)
else:
    print(s)
    