n=int(input())
m=list(map(int,input().split()))
k=0
for i in range(1,len(m)-1):
    if m[i-1]%2!=0 and m[i+1]%2!=0 and m[i]%2!=0:
        k+=1
   
print(k)