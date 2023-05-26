n=int(input())
l=list(map(int,input().split()))
k=0
a=set(l)
s=list(a)
for i in a:
    if s.count(i)==1:
        k+=i
#if l==[1,2,3,4,5,6,7]:
print(k)
#else:
   # print(k,l)