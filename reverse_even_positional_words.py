n=input()
l=list(n.split())
a=[]
for i in range(len(l)):
    if i%2==0:
        k=l[i]
        a.append(k[::-1])
    elif i%2!=0:
        a.append(l[i])
print(*a)
        