def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
sum=0
temp=a
while a>0:
    d=a%10
    sum=sum*10+d
    a//=10
if prime(sum) and prime(temp):
    print("circular prime")
elif prime(temp):
    print('prime but not a circular prime')
else:
    print('not prime')