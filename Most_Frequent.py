n=int(input())
z=list(map(int,input().split()))
l=[]
j=0
z.sort()
for i in z:
    k=z.count(i)
    if k>j:
        h=i
        j=k
print(h)
    