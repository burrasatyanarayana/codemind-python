n=input()
a="1234567890"
k=0
for i in n:
    if i in a:
        k+=1
if k==0:
    print("Doesn't contain digit")
else:
    print(f"Contains {k} digit")