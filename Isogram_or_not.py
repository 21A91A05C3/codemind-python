n=input()
v=0
for i in n:
    if n.count(i)==1:
        v+=1
if len(n)==v:
    print("True")
else:
    print("False")
        