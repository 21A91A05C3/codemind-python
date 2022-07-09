n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    k=str(i)
    k=len(k)
    a.append(k)
c=0
for i in a:
    if min(a)==i:
        c+=1
print(c)
        