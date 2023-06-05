n=input()
j=0
q='aeiouAEIOU'
g=n
a=len(g)-1
b=0
while a>=b:
    if g[a]!=chr(32) and g[b]!=chr(32):
        if (g[b] in q and g[a] not in q ) or (g[a]  in q and g[b] not  in q):
            j+=1
            a-=1
            b+=1
        else:
            a-=1
            b+=1
    else:
        a-=1
        b+=1
        
print(j)
