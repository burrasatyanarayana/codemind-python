n=int(input())
l=list(map(int,input().split()))
o=0
for i in range(len(l)):
    if l[i]%2!=0:
        break
    o+=l[i]
         
print(o)