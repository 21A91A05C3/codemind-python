n=input()
s=''
c=[]
d=[]
for i in range(len(n)):
    if n[i].isalnum():
        s+=n[i]
    else:
        c.append(i)
        d.append(n[i])
s=sorted(s)
# print(s)
for i in range(len(c)):
    s.insert(c[i],d[i])
print(''.join(s))