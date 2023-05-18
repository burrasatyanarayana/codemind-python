n=int(input())
l=list(map(int,input().split()))
z=l[::-1]
j=0
for i in z:
    j+=1
    if i%2==0:
        print(len(l)-j)
        break