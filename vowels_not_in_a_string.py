n=input()
z='aeiou'
k=''
s=''
for i in n:
    if i  in z:
        if i not in k:
            k+=i
for i in z:
    if i not in k:
        s+=i
if len(s)==0:
    print(0)
else:
    for j in s:
        print(j,end=' ')
    