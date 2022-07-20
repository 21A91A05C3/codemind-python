n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if l.count(i)==1 and i!=' ' and i not in k:
        k.append(i)
        c+=1
if c>0:
    print(max(k))
else:
    print(-1)