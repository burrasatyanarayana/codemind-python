n=input()
a='AEIOUaeiou'
k=''
x='AEIOU'
y='aeiou'
w=''
o=''
for i in n:
    if i in a:
            k+=i
if len(k)==0:
    print(0)
else:
    print(len(k))