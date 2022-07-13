n=input()
k='aeiou'
l=[]
c=0
for i in n:
    if i in k and i not in l:
        l.append(i)
        c+=1
if c==len(k):
    print("True")
else:
    print("False")