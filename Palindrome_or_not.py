def hh(z):
    m=z[::-1]
    if z==m:
        return True
    else:
        return False
n=input()
a=n.lower()
x=0
d=hh(a)
print(d)