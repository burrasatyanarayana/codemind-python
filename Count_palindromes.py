def gg(i):
    s=str(i)
    x=s[::-1]
    if s==x:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
z=0
for i in l:
    x=gg(i)
    z+=x
print(z)