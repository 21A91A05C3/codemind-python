n=input()
l=[]
for i in n.split():
    x=i
    x=x[::-1]
    l.append(x)
print(*l)