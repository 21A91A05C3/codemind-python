n=input()
c=0
l=[]
for i in set(n):
    if i in 'aeiou':
        l.append(i)
        c+=1
if  5==len(l):
    print("True")
else:
    print("False")
# print(l)