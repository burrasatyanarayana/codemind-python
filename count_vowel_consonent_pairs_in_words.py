n=input().split()
j=0
q='aeiouAEIOU'
for i in n:
    g=list(i)
    a=len(g)-1
    b=0
    while b<a:
        if (g[b] in q and g[a] not in q) or (g[a]  in q and g[b] not  in q) :
            j+=1
            a-=1
            b+=1
        else:
            a-=1
            b+=1
print(j)
