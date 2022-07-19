n=input().lower()
k=[]
for i in n:
    if i!=' ':
        k.append(i)
print(len(set(k)))