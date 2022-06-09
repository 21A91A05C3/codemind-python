def prime(i):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c+=1
    if c==0:
        return 1
def palindrome(i):
    temp=i
    rev=0
    while(i):
        d=i%10
        rev=rev*10+d
        i=i//10
    if temp==rev:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,n*n):
    if prime(i)==1 and palindrome(i)==1:
        print(i)
        break
     