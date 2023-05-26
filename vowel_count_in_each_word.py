n=input().split(' ')
l=list(n)
a='AEIOUAaeiou'
k=[]
q=''
for i in l:
    g=0
    for j in i:
        if j in a:
            g+=1
    k.append(g)
print(*k)  