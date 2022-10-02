n=input()
s=""
k=[]
for i in range(len(n)):
    if n[i]==".":
        k.append('[.]')
    else:
        k.append(n[i])
print("".join(k))