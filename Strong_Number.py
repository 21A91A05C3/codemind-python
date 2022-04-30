n=int(input())
temp=n
sum=0
while n:
    i=1
    fact=1
    rem=n%10
    while i<=rem:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==temp:
    print('The number',temp,'is a strong number')
else:
    print('The number',temp,'is not a strong number')
