n=int(input())
l=list(map(int,input().split()))
z=l[::-1]
for i in z:
    if i%2!=0:
        print(i)
        break