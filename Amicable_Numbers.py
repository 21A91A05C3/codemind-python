a=int(input())
b=int(input())
sum=0
sum1=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
for j in range(1,b):
    if(b%j==0):
        sum1=sum1+j
if(sum==b and sum1==a):
    print("Amicable")
else:
    print("Not Amicable")