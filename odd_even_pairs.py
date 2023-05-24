n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
for i in range(len(l)):
    if i<len(l2):
        l3.append(l2[i])
    if i<len(l1):
        l3.append(l1[i])
if len(l)%2!=0:
    l3.append(0)
print(*l3)