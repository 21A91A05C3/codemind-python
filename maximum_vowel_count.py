n=input().lower()
k='AEIOUaeiou'
l=[]
for i in n.split():
    c=0
    for j in i:
        if j in k:
            c+=1
        l.append(c)
print(max(l))

