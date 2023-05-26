n=input()
a='AEIOUaeiou'
k=''
x='AEIOU'
y='aeiou'
w=''
o=''
for i in n:
    if i in x:
        if i not in k:
            k+=i
    if i in y:    
        if i not in w:
            w+=i
if len(w)==5 or  len(o)==5:
    print(True)
else:
        print(False)
    