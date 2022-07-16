n=input().lower()
m=input().lower()
for i in m.split():
    if i in n.split():
        print(i,end=' ')