def prime(n):
    if n<2:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
l=list(map(int,input().split()))
a=min(l)
b=max(l)
z=l.index(a)
x=l.index(b)
a=max(z,x)
b=min(z,x)
for i in range(b,a+1):
    if(prime(l[i])):
        c+=1
# print(l)
print(c)