n=input().lower()
k=[]
j=[]
for i in n.split():
    k.append(ord(min(i)))
    j.append(ord(max(i)))
print(abs(sum(k)-sum(j)))
        