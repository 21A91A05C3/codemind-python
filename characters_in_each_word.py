n=input()
k=[]
for i in n.split():
    k.append(len(i)) 
print(*k)