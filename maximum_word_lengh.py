n=input()
h=[]
k=[]
for i in n.split():
    h.append(i)
    x=len(i)
    k.append(x)
print(max(k))
    