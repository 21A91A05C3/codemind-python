m=int(input())
b=[]
l=list(map(int,input().split()))
v=0
for i in l:
    if i==l.count(i) and i not in b:
        b.append(i)
        v+=1
if v==0:
    print(-1)
else:
    print(min(b),max(b))
