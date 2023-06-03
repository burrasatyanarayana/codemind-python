a,b,c=map(int,input().split())
h=0
for i in range(a,b+1):
    if i%c==0:
        h+=1
print(h)
        
