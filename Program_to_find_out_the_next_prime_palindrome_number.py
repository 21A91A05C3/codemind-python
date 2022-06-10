def prime(n):
    if n==1:
        return 0
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c+=1
    if(c==0):
        return 1
def pali(n):
    if(str(n)==(str(n)[::-1])):
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,n*n):
    if(prime(i)==1 and pali(i)==1):
        print(i)
        break