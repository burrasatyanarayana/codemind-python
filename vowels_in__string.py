n=input()
z='aeiouAEIOU'
k=''
for i in n:
    if i  in z:
        if i not in k:
            k+=i
if len(k)==0:
    print(-1)
else:
    for j in k:
        print(j,end=' ')
    