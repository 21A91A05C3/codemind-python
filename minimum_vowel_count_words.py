n=input().lower().split()
l=[]
k='aeiou'
for i in n:             
    x=i
    c=0
    for i in x:
        if i in k and i not in l:
           c+=1
    l.append(c)
v=min(l)
c=0
for i in l:
    if v==i:
        c+=1
print(c)