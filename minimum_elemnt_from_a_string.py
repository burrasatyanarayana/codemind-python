n=input().split(' ')
z=n[-1]
f=min(z)

if 65<=ord(f)<=90:
    q=chr(ord(f)+32)
    if q in z:
        print(q)
    else:
        print(f)
else:
    print(f)