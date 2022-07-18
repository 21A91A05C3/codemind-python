n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if i==l.count(i) and i not in a:
        a.append(i)
        c+=1

if c>0:
    print(*a)
elif c==0:
    print(-1)
