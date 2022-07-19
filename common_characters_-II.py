n=input().lower()
m=input().lower()
k=[]
for i in n:
    if i in m and i!=' ':
        k.append(i)
g=set(k)
print(len(g))