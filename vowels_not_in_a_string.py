n=input()
k='aeiou'
c=0
l=[]
for i in k:
    if i not in n:
        l.append(i)
        c+=1
if c>0:
    print(*l)
else:
    print(0)