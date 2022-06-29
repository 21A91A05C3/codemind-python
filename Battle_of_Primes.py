def prime(n):
    if n==1:
        return 0
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    else:
        return 0
n=int(input())
m=int(input())
x=n+m
i=1
while(1):
    if prime(x+i)==1:
        print(i)
        break
    i+=1