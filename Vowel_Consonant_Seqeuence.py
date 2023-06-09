n=input()
a="aeiou"
v=[]
for i in range(len(n)-1):
    if n[i] in  a  and n[i+1] in a:
        continue
    if n[i]  not in  a  and n[i+1] not in a:
        continue
    if n[i] in a:
        v.append("V")
    else:
        v.append("C")
if n[-1] in a:
    v.append("V")
else:
    v.append("C")
d=''.join(v)
print(d)
        