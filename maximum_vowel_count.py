n=input().lower().split()
z=[]
k=''
for i in n:
    h=0
    for j in i:
        if j in 'aeiou':
            h+=1
    z.append(h)
print(max(z))
    