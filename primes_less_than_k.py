def prime(i):
    c=0
    d=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0:
        d+=1
    return d
            
l=[]        
k=[]
n=int(input())
arr=list(map(int,input().split()))
a=int(input())
for i in arr:
    if i<=a and i!=1:
        l.append(i)
for i in l:
    k.append(prime(i))
print(sum(k))