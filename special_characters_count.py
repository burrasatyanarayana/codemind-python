n=input().lower()
k=0
for i in n:
    if 97<=ord(i)<=122 or i==' ':
        continue
    k+=1
print(k)
    