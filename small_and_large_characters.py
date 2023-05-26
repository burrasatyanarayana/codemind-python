n=input().split(' ')
z=list(n)
l=[]
for i in z:
    q=list(i)
    a=min(q)
    b=max(q)
    #print(min(a),max(b))
    l.append(a)
    l.append(b)
print(*l)