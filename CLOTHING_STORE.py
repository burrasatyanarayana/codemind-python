n=int(input())
m=list(map(int,input().split()))
b=''
z=[]
k=0
for i in m:
    if str(i) not in b:
         z.append(m.count(i))
         b+=str(i)
for i in z:
    k+=(i//2)
print(k)

