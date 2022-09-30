n=int(input())
l=list(map(int,input().split()))
c=1
b=[]
for j in range(len(l)):
    c=1
    for i in range(len(l)):
        if l[i]!=l[j]:
            c*=l[i]
    b.append(c)
print(*b)