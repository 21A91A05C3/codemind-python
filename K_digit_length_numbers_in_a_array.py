n,m=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in l:
    j=abs(i)
    k=str(j)
    k=len(k)
    a.append(k)
c=0
for i in a:
    if m==i:
        c+=1
print(c)
