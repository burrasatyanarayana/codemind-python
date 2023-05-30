n=input()
m=list(n)
s=" !@#$%^&*()"
l=[]
for i in  range(len(m)):
    if m[i] not in s:
        l.append(m[i])
        m[i]='*'
l.sort()
k=0
for i in range(len(m)):
    if m[i]=='*':
        m[i]=l[k]
        k+=1
a=''.join(m)
print(a)
        
        


 