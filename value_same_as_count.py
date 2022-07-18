n=int(input())
l=list(map(int,input().split()))
k=[]
v=0
for i in l:
    if l.count(i)==i and i not in k:
        k.append(i)
        v+=1
print(v)