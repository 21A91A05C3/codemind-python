n=int(input())
m=int(input())
l=[]
for i in range(n,m):
    temp=i
    rev=0
    while(i):
        d=i%10
        rev=rev*10+d
        i=i//10
    if(temp==rev):
        l.append(rev)
print(*l)