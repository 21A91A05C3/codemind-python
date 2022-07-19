n=input().lower()
k=[]
for i in n:
    if i!=' ':
        k.append(i)
j=set(k)
print("".join(sorted(j)))