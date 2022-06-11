def prime(n):
    for i in range(1,n):
        for j in range(i+1,n):
            if i*j==n:
                return i,j
    else:
        return 0
n=int(input())
l=prime(n)
if l==0:
    print(-1)
else:
    print(*l)