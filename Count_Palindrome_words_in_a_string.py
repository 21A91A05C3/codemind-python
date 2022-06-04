s=input()
l=[]
s=s.lower()
for i in s.split():
    if i==i[::-1]:
        l.append(i)
print(len(l))