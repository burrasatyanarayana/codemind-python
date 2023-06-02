n=int(input())
m=list(map(int,input().split()))
l=[]
k=0
h=0
for i in range(0,len(m)-2,1):
    if m[i]<m[i+1] and m[i+1]>m[i+2] or m[i]>m[i+1] and m[i+1]<m[i+2] :
        k+=1
    else:
        h=1
if len(m)==k+2:
    print('yes')
else:
    print('no',)