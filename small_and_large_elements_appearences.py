n=input()
a=[]
b=[]
for i in n :
    if i!=' ':
        a.append(n.count(i))
        b.append(ord(i))
k=chr(min(b))
k1=chr(max(b))
print(k,n.count(k),k1,n.count(k1))

