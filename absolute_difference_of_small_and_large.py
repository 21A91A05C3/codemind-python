n=input()
k=[]
for i in n.split():
    x=i
    g=min(x)
    g1=max(x)
    k.append(abs(ord(g)-ord(g1)))
print(*k)