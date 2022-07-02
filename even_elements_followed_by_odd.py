m=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    if l[i]%2==0:
        a.append(l[i])
for i in range(len(l)):
    if l[i]%2!=0:
        a.append(l[i])
print(*a)