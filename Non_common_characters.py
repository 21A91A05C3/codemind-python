n=input().lower()
m=input().lower()
l=[]
for i in n:
    if i not in m and i not in l and i!=' ':
        l.append(i)
for i in m:
    if i not in n and i not in l and i!=' ':
         l.append(i)
k="".join(sorted(l))
print(len(k))