m,n=map(int,input().split())
c=0
ml=list(map(int,input().split()))
nl=list(map(int,input().split()))
for i in set(ml):
    if i not in nl:
        c+=1
for i in set(nl):
    if i not in ml:
        c+=1
print(c)