n=int(input())
arr=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
l=[]
k=[]
m=[]
c=0
for i in arr:
    k.append(i)
for i in range(a,b+1):
    l.append(i)
for i in k:
    if i not in l:
        m.append(i)
        c+=1
if c>0:
    print(min(m))#
else:
    print("-1")
    
    