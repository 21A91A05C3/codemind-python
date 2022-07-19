n=int(input())
l=list(map(int,input().split()))
k=[]
c=[]
for i in l:
    if i not in c:
        c.append(i)
        k.append(i)
        k.append(l.count(i))
print(*k)