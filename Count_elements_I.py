n,m=map(int,input().split())
l=list(map(int,input().split()))
f=list(map(int,input().split()))
d=set(l)
e=set(f)
z=d.intersection(e)

print(len(z))