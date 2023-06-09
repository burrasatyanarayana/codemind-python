n=int(input())
m=list(map(str,input().split()))
z=''.join(m)
x=z.split("0")
l=[]
for i in x:
    l.append(len(i))
print(max(l))