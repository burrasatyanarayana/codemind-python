n=int(input())
m=list(map(int,input().split()))
l=[]
k=0
m.append(m[0])
m.append(m[1])
for i in range(1,len(m)-1):
    if m[i-1]%2==0 and m[i+1]%2!=0:
        l.append(m[i])
        k+=1
    elif m[i-1]%2!=0 and m[i+1]%2==0:
        l.append(m[i])
        k+=1
print(k)