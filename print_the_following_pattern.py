n=int(input())
d=0
for i in range(1,n+1):
    val=i+n+d
    d-=2
    for j in range(1,val):
        print(j,end='')
    print()