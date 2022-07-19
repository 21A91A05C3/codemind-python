n=input()
l=[]
k=[]
for i in n:
    if i=='z':
        l.append(i)
    else:
        k.append(i)
# print(len(l),len(k))
if len(k)==2*len(l):
    print("Yes")
else:
    print("No")
# print(len(k))