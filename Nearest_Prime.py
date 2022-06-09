def prime(i):
    if i==1:
        return 0
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0:
        return i
n=int(input())
for i in range(n):
    m=int(input())
    for i in range(m,0,-1):
        if prime(i):
            l=i
            break
    for i in range(m+1,m*m):
        if prime(i):
            k=i
            break
    if (k-m)>=(m-l):
        print(l)
    else:
        print(k)