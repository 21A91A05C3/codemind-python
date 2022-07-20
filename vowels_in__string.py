n=input()
v=set('aeiouAEIOU')
l=[]
for i in range(0,len(n)):
    if n[i] in v:
        l.append(n[i])
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(*r)