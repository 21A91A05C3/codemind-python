n=int(input())
l=list(map(int,input().split()))
b=[]
v=0
for i in l:
    if l.count(i)==i and i not in b:
        b.append(i)
        v+=1
if v==0:
    print(-1)
else:
    print('{:.2f}'.format(sum(b)/len(b)))