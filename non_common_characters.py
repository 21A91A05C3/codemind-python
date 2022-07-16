n=input().lower()
m=input().lower()
'''k=set(n)
k1=set(m)
l=[]
for i in k:
    if i not in k1:
        l.append(i)
for i in k1:
    if i not in k:
        l.append(i)
d=[]
for i in l:
    d.append(ord(i))
k=sorted(d)
for i in k:
    print(chr(i),end="")'''
l=[]
for i in n:
    if i not in m and i not in l and i!=' ':
        l.append(i)
for i in m:
    if i not in n and i not in l and i!=' ':
        l.append(i)
print("".join(sorted(l)))