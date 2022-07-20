n=input().lower()
l=[]
for i in n:
    if n.count(i)==1 and i!=' ':
        l.append(i)
print("".join(sorted(l)))