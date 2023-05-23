n=input()
l=[]
k=0
for i in n:
    l.append(i)
for j in l:
    if l.count(j)==1:
        k+=1
if k==len(l):
    print(True)
else:
    print(False)