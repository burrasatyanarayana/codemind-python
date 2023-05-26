n=input().split(' ')
t='AEIOUaeiou'
z=list(n)
b=0
for i in z:
    if i[0] in t:
        if  i[len(i)-1] not in t:
            b+=1
print(b)    
