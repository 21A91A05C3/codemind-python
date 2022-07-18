n=input().lower()
v=0
for i in n.split():
    if i==i[::-1]:
        v+=1
print(v)