n=int(input())
l=list(map(int,input().split()))
k=[]
v=0
m=int(input())
for i in l:
    if l.count(i)==m and i not in k:
        k.append(i)
        v+=1
if v>0:
    print(*k)
else:
    print(-1)