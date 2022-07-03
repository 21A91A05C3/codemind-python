def prime(i):
    c=0
    d=0
    if i==1:
        return 0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0:
        d+=1
    return d
n=int(input())
sum=0
k=[]
c=0
l=list(map(int,input().split()))
for i in l:
    if prime(i)==1:
        c+=1
        sum=sum+i
k=sum
print('{:.2f}'.format(int(k)/c))
    